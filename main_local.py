"""Main application for LOCAL Voice-Based AI Agent (NO API KEY REQUIRED!)."""

import sys
from agent.core_local import LocalVoiceAgent
from voice.speech_to_text_local import LocalSpeechToText
from voice.text_to_speech_local import LocalTextToSpeech
from memory.store import MemoryStore


def print_banner():
    """Print welcome banner."""
    print("\n" + "="*60)
    print("🤖 Voice-Based AI Agent (LOCAL VERSION - NO API KEY!)")
    print("="*60)
    print("Features:")
    print("  ✅ To-Do Management (add, list, update, delete)")
    print("  🧠 Memory System (save and recall information)")
    print("  🎤 Voice Interface (100% local, no API key needed)")
    print("  🔒 Privacy: Everything runs on your computer")
    print("="*60)
    print("\nUsing:")
    print("  🦙 Ollama (local LLM)")
    print("  🎤 Google Speech Recognition (free)")
    print("  🔊 pyttsx3 (offline TTS)")
    print("="*60 + "\n")


def print_menu():
    """Print interaction menu."""
    print("\n📋 Options:")
    print("  1. Voice input (record and speak)")
    print("  2. Text input (type your message)")
    print("  3. View memory stats")
    print("  4. Reset conversation")
    print("  5. Exit")
    print()


def main():
    """Main application loop."""
    print_banner()
    
    # Initialize components
    print("🔧 Initializing components...\n")
    
    try:
        # Initialize agent (will check if Ollama is running)
        agent = LocalVoiceAgent(
            model="llama3.2",  # or "mistral", "llama2", etc.
            ollama_url="http://localhost:11434"
        )
        
        # Initialize voice components
        print("\n🎤 Initializing speech recognition...")
        stt = LocalSpeechToText()
        
        print("\n🔊 Initializing text-to-speech...")
        tts = LocalTextToSpeech(rate=150, volume=0.9)
        
        memory_store = MemoryStore()
        
        print("\n✅ All components initialized successfully!\n")
    except Exception as e:
        print(f"\n❌ Error initializing components: {e}")
        print("\nMake sure Ollama is installed and running:")
        print("  1. Download from: https://ollama.ai")
        print("  2. Run: ollama serve")
        print("  3. Run: ollama pull llama3.2")
        sys.exit(1)
    
    # Main interaction loop
    while True:
        try:
            print_menu()
            choice = input("Choose an option (1-5): ").strip()
            
            if choice == "1":
                # Voice input mode
                print("\n🎤 Voice Input Mode")
                
                user_input = stt.listen_continuous()
                
                if not user_input:
                    print("❌ No speech detected or transcription failed")
                    continue
                
                print(f"\n👤 You said: {user_input}\n")
                
                # Process with agent
                print("🤔 Agent is thinking...")
                response = agent.process_message(user_input)
                
                print(f"\n🤖 Agent: {response}\n")
                
                # Speak response
                tts.speak(response, play_audio=True)
            
            elif choice == "2":
                # Text input mode
                print("\n⌨️  Text Input Mode")
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Process with agent
                print("\n🤔 Agent is thinking...")
                response = agent.process_message(user_input)
                
                print(f"\n🤖 Agent: {response}\n")
                
                # Ask if user wants to hear the response
                speak_choice = input("Speak response? (y/n): ").strip().lower()
                if speak_choice == "y":
                    tts.speak(response, play_audio=True)
            
            elif choice == "3":
                # View memory stats
                print("\n📊 Memory Statistics")
                stats = memory_store.get_memory_stats()
                print(f"  Total memories: {stats['total_memories']}")
                print(f"  Categories: {stats['categories']}")
                print(f"  Oldest: {stats['oldest_memory']}")
                print(f"  Newest: {stats['newest_memory']}")
                
                # Show recent memories
                recent = memory_store.get_recent_memories(count=3)
                if recent:
                    print("\n  Recent memories:")
                    for mem in recent:
                        print(f"    - [{mem['category']}] {mem['content'][:60]}...")
            
            elif choice == "4":
                # Reset conversation
                agent.reset_conversation()
                print("✅ Conversation history cleared")
            
            elif choice == "5":
                # Exit
                print("\n👋 Goodbye!")
                tts.cleanup()
                break
            
            else:
                print("❌ Invalid choice. Please choose 1-5.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted by user. Goodbye!")
            tts.cleanup()
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Continuing...\n")


if __name__ == "__main__":
    main()
