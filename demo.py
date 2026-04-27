"""
Voice AI Agent Demo - Simple & Fast
Direct tool usage for instant responses
"""

import json
import os
from datetime import datetime

# Setup data directory
DATA_DIR = "data"
TODOS_FILE = os.path.join(DATA_DIR, "todos.json")
MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize files
if not os.path.exists(TODOS_FILE):
    with open(TODOS_FILE, 'w') as f:
        json.dump([], f)

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, 'w') as f:
        json.dump([], f)


def load_todos():
    with open(TODOS_FILE, 'r') as f:
        return json.load(f)


def save_todos(todos):
    with open(TODOS_FILE, 'w') as f:
        json.dump(todos, f, indent=2)


def load_memories():
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)


def save_memories(memories):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memories, f, indent=2)


def add_task(description):
    todos = load_todos()
    new_id = max([t.get('id', 0) for t in todos], default=0) + 1
    new_todo = {
        'id': new_id,
        'description': description,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    todos.append(new_todo)
    save_todos(todos)
    return new_todo


def list_tasks():
    return load_todos()


def complete_task(task_id):
    todos = load_todos()
    for todo in todos:
        if todo['id'] == task_id:
            todo['completed'] = True
            todo['updated_at'] = datetime.now().isoformat()
            save_todos(todos)
            return True
    return False


def delete_task(task_id):
    todos = load_todos()
    todos = [t for t in todos if t['id'] != task_id]
    save_todos(todos)
    return True


def save_memory(content):
    memories = load_memories()
    new_id = max([m.get('id', 0) for m in memories], default=0) + 1
    new_memory = {
        'id': new_id,
        'content': content,
        'timestamp': datetime.now().isoformat()
    }
    memories.append(new_memory)
    save_memories(memories)
    return new_memory


def recall_memories():
    return load_memories()


print("\n" + "="*60)
print("🤖 Voice AI Agent - Demo")
print("="*60)
print("\n📋 Commands: add, list, done, delete, remember, recall, quit\n")

while True:
    try:
        user_input = input("👤 You: ").strip()
        
        if not user_input:
            continue
        
        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        if command in ['quit', 'exit']:
            print("\n👋 Goodbye!\n")
            break
        
        elif command == 'add':
            if not args:
                print("❌ Usage: add <task>")
                continue
            task = add_task(args)
            print(f"✅ Added task #{task['id']}: {args}")
        
        elif command == 'list':
            tasks = list_tasks()
            if not tasks:
                print("📋 No tasks yet!")
            else:
                print(f"\n📋 Your Tasks ({len(tasks)} total):")
                print("-" * 60)
                for task in tasks:
                    status = "✓" if task['completed'] else "○"
                    print(f"  {status} #{task['id']}: {task['description']}")
                print("-" * 60)
        
        elif command == 'done':
            if not args:
                print("❌ Usage: done <id>")
                continue
            try:
                task_id = int(args)
                if complete_task(task_id):
                    print(f"✅ Marked task #{task_id} as completed!")
                else:
                    print(f"❌ Task #{task_id} not found")
            except ValueError:
                print("❌ ID must be a number")
        
        elif command == 'delete':
            if not args:
                print("❌ Usage: delete <id>")
                continue
            try:
                task_id = int(args)
                delete_task(task_id)
                print(f"🗑️  Deleted task #{task_id}")
            except ValueError:
                print("❌ ID must be a number")
        
        elif command == 'remember':
            if not args:
                print("❌ Usage: remember <info>")
                continue
            memory = save_memory(args)
            print(f"🧠 Remembered: {args}")
        
        elif command == 'recall':
            memories = recall_memories()
            if not memories:
                print("🧠 No memories yet!")
            else:
                print(f"\n🧠 Your Memories ({len(memories)} total):")
                print("-" * 60)
                for mem in memories:
                    print(f"  #{mem['id']}: {mem['content']}")
                print("-" * 60)
        
        else:
            print(f"❌ Unknown command: '{command}'")
    
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        break
    except Exception as e:
        print(f"❌ Error: {e}")
