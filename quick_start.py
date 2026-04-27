"""Quick start script - Simple text-based AI agent (NO API KEY!)"""

from agent.core_local import LocalVoiceAgent

print("="*60)
print("🤖 Voice AI Agent - Quick Start (Text Only)")
print("="*60)
print("\n✅ Using Ollama (local, free, no API key)")
print("✅ All features work: To-Do + Memory")
print("✅ Type 'quit' to exit\n")

# Initialize agent
try:
    print("🔧 Initializing agent...")
    agent = LocalVoiceAgent(model="llama3.2")
    print("✅ Ready!\n")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure Ollama is running!")
    print("  In Ollama app, click 'Launch' or run: ollama serve")
    exit(1)

# Main loop
while True:
    try:
        user_input = input("\n👤 You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\n👋 Goodbye!")
            break
        
        print("\n🤔 Agent thinking...")
        response = agent.process_message(user_input)
        print(f"\n🤖 Agent: {response}")
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Continuing...\n")
