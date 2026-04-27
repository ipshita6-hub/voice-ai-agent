"""Ultra-simple quick start - Faster responses"""

import requests
import json
from agent.tools import execute_function

print("="*60)
print("🤖 Voice AI Agent - Simple Mode (Faster)")
print("="*60)
print("\nCommands:")
print("  add: <task>     - Add a task")
print("  list            - List all tasks")
print("  done: <id>      - Mark task as done")
print("  remember: <info> - Save to memory")
print("  recall          - Show memories")
print("  quit            - Exit\n")

while True:
    try:
        user_input = input("\n👤 You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() in ['quit', 'exit']:
            print("\n👋 Goodbye!")
            break
        
        # Simple command parsing (no AI needed!)
        if user_input.startswith("add:"):
            task = user_input[4:].strip()
            result = execute_function("add_todo", {"description": task})
            print(f"\n✅ Added: {task}")
        
        elif user_input == "list":
            result = execute_function("list_todos", {})
            todos = result.get('todos', [])
            if todos:
                print(f"\n📋 Your tasks ({len(todos)}):")
                for todo in todos:
                    status = "✓" if todo['completed'] else "○"
                    print(f"  {status} {todo['id']}. {todo['description']}")
            else:
                print("\n📋 No tasks yet!")
        
        elif user_input.startswith("done:"):
            task_id = int(user_input[5:].strip())
            result = execute_function("update_todo", {"todo_id": task_id, "completed": True})
            print(f"\n✅ Marked task {task_id} as done!")
        
        elif user_input.startswith("remember:"):
            info = user_input[9:].strip()
            result = execute_function("save_memory", {"content": info, "category": "general"})
            print(f"\n🧠 Remembered: {info}")
        
        elif user_input == "recall":
            result = execute_function("recall_memory", {})
            memories = result.get('memories', [])
            if memories:
                print(f"\n🧠 Your memories ({len(memories)}):")
                for mem in memories:
                    print(f"  • {mem['content']}")
            else:
                print("\n🧠 No memories yet!")
        
        else:
            print("\n❌ Unknown command. Try: add:, list, done:, remember:, recall")
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        break
    except Exception as e:
        print(f"\n❌ Error: {e}")
