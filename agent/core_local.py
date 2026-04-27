"""Local agent using Ollama (no API key required)."""

import json
import re
from typing import List, Dict
import requests
from agent.prompt import get_system_prompt
from agent.tools import TOOLS, execute_function


class LocalVoiceAgent:
    """Voice-based AI agent using local Ollama model."""
    
    def __init__(self, model: str = "llama3.2", ollama_url: str = "http://localhost:11434"):
        """
        Initialize the local agent.
        
        Args:
            model: Ollama model name (llama3.2, mistral, etc.)
            ollama_url: Ollama API endpoint
        """
        self.model = model
        self.ollama_url = ollama_url
        self.conversation_history: List[Dict] = []
        self.system_prompt = get_system_prompt()
        
        # Check if Ollama is running
        self._check_ollama()
    
    def _check_ollama(self):
        """Check if Ollama is running and model is available."""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags")
            if response.status_code == 200:
                models = response.json().get('models', [])
                model_names = [m['name'] for m in models]
                if not any(self.model in name for name in model_names):
                    print(f"⚠️  Model '{self.model}' not found. Available models: {model_names}")
                    print(f"   Run: ollama pull {self.model}")
                else:
                    print(f"✅ Ollama is running with model: {self.model}")
        except requests.exceptions.ConnectionError:
            print("❌ Ollama is not running!")
            print("   Please install and start Ollama:")
            print("   1. Download from: https://ollama.ai")
            print("   2. Run: ollama serve")
            print(f"   3. Run: ollama pull {self.model}")
            raise
    
    def _create_tool_description(self) -> str:
        """Create a text description of available tools."""
        tool_desc = "\n\nYou have access to these tools:\n\n"
        
        for tool in TOOLS:
            func = tool['function']
            tool_desc += f"**{func['name']}**: {func['description']}\n"
            tool_desc += f"Parameters: {json.dumps(func['parameters']['properties'], indent=2)}\n\n"
        
        tool_desc += """
To use a tool, respond with:
TOOL_CALL: function_name
ARGUMENTS: {"param1": "value1", "param2": "value2"}

After tool results, provide a natural response to the user.
"""
        return tool_desc
    
    def _call_ollama(self, messages: List[Dict]) -> str:
        """Call Ollama API."""
        # Combine messages into a single prompt
        prompt = f"{self.system_prompt}\n{self._create_tool_description()}\n\n"
        
        for msg in messages:
            role = msg['role']
            content = msg['content']
            
            if role == 'user':
                prompt += f"\nUser: {content}\n"
            elif role == 'assistant':
                prompt += f"\nAssistant: {content}\n"
            elif role == 'tool':
                prompt += f"\nTool Result: {content}\n"
        
        prompt += "\nAssistant: "
        
        # Call Ollama
        response = requests.post(
            f"{self.ollama_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )
        
        if response.status_code != 200:
            raise Exception(f"Ollama API error: {response.text}")
        
        return response.json()['response']
    
    def _parse_tool_calls(self, response: str) -> List[Dict]:
        """Parse tool calls from model response."""
        tool_calls = []
        
        # Look for TOOL_CALL pattern
        pattern = r'TOOL_CALL:\s*(\w+)\s*ARGUMENTS:\s*(\{[^}]+\})'
        matches = re.finditer(pattern, response, re.DOTALL)
        
        for match in matches:
            function_name = match.group(1).strip()
            try:
                arguments = json.loads(match.group(2).strip())
                tool_calls.append({
                    'function_name': function_name,
                    'arguments': arguments
                })
            except json.JSONDecodeError:
                print(f"⚠️  Failed to parse arguments: {match.group(2)}")
        
        return tool_calls
    
    def _extract_response(self, text: str) -> str:
        """Extract the natural response (remove tool call syntax)."""
        # Remove TOOL_CALL and ARGUMENTS sections
        text = re.sub(r'TOOL_CALL:.*?ARGUMENTS:.*?\}', '', text, flags=re.DOTALL)
        return text.strip()
    
    def process_message(self, user_message: str) -> str:
        """
        Process a user message and return the agent's response.
        
        Args:
            user_message: The user's input message
        
        Returns:
            The agent's response text
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Get initial response
        response = self._call_ollama(self.conversation_history)
        
        # Check for tool calls
        tool_calls = self._parse_tool_calls(response)
        
        if not tool_calls:
            # No tool calls, return response directly
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            return response
        
        # Execute tool calls
        tool_results = []
        for tool_call in tool_calls:
            function_name = tool_call['function_name']
            arguments = tool_call['arguments']
            
            print(f"[Tool Call] {function_name}({arguments})")
            
            # Execute the function
            result = execute_function(function_name, arguments)
            tool_results.append({
                'function': function_name,
                'result': result
            })
            
            # Add to history
            self.conversation_history.append({
                "role": "tool",
                "content": f"Tool {function_name} returned: {json.dumps(result)}"
            })
        
        # Get final response after tool execution
        final_response = self._call_ollama(self.conversation_history)
        final_response = self._extract_response(final_response)
        
        self.conversation_history.append({
            "role": "assistant",
            "content": final_response
        })
        
        return final_response
    
    def reset_conversation(self):
        """Clear the conversation history."""
        self.conversation_history = []
        print("[Agent] Conversation history cleared")
