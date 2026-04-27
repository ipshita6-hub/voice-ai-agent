"""Test script for the LOCAL AI agent (no API key required)."""

from agent.core_local import LocalVoiceAgent
from memory.store import MemoryStore


def print_separator():
    """Print a visual separator."""
    print("\n" + "="*70 + "\n")


def test_agent():
    """Test the agent with various commands."""
    print("🔧 Initializing local agent...")
    
    try:
        agent = LocalVoiceAgent(model="llama3.2")
        memory_store = MemoryStore()
        
        print("✅ Agent initialized!\n")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure Ollama is running:")
        print("  1. Download from: https://ollama.ai")
        print("  2. Run: ollama serve")
        print("  3. Run: ollama pull llama3.2")
        return
    
    # Test scenarios
    test_scenarios = [
        # To-Do Management
        "Add a task to buy groceries tomorrow",
        "Add another task to call mom with high priority",
        "What's on my to-do list?",
        "Mark task 1 as completed",
        "Show me only incomplete tasks",
        
        # Memory System
        "My favorite color is blue and I love pizza",
        "I have an important meeting with the client next Tuesday at 3 PM",
        "What do you remember about my preferences?",
        
        # Conversational
        "How many tasks do I have?",
    ]
    
    print("🧪 Running test scenarios...\n")
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"Test {i}/{len(test_scenarios)}")
        print(f"👤 User: {scenario}")
        
        try:
            response = agent.process_message(scenario)
            print(f"🤖 Agent: {response}")
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print_separator()
        
        # Pause between tests
        input("Press Enter to continue to next test...")
    
    # Show final stats
    print("\n📊 Final Statistics")
    print("\nMemory Stats:")
    stats = memory_store.get_memory_stats()
    print(f"  Total memories: {stats['total_memories']}")
    print(f"  Categories: {stats['categories']}")
    
    print("\n✅ All tests completed!")


if __name__ == "__main__":
    test_agent()
