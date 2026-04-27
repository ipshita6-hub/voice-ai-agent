"""Tool definitions and implementations for the AI agent."""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# Data directory setup
DATA_DIR = "data"
TODOS_FILE = os.path.join(DATA_DIR, "todos.json")
MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)


# ============================================================================
# To-Do Management Functions
# ============================================================================

def load_todos() -> List[Dict]:
    """Load todos from file."""
    if not os.path.exists(TODOS_FILE):
        return []
    try:
        with open(TODOS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_todos(todos: List[Dict]) -> None:
    """Save todos to file."""
    with open(TODOS_FILE, 'w') as f:
        json.dump(todos, f, indent=2)


def add_todo(description: str, due_date: Optional[str] = None, priority: str = "medium") -> Dict:
    """
    Add a new todo item.
    
    Args:
        description: The task description
        due_date: Optional due date in YYYY-MM-DD format
        priority: Priority level (low, medium, high)
    
    Returns:
        Dict with success status and the created todo
    """
    todos = load_todos()
    
    # Generate new ID
    new_id = max([t.get('id', 0) for t in todos], default=0) + 1
    
    new_todo = {
        'id': new_id,
        'description': description,
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'due_date': due_date,
        'priority': priority
    }
    
    todos.append(new_todo)
    save_todos(todos)
    
    return {
        'success': True,
        'message': f'Added todo: {description}',
        'todo': new_todo
    }


def list_todos(filter_completed: Optional[bool] = None) -> Dict:
    """
    List all todos, optionally filtered by completion status.
    
    Args:
        filter_completed: If True, show only completed. If False, show only incomplete. If None, show all.
    
    Returns:
        Dict with success status and list of todos
    """
    todos = load_todos()
    
    if filter_completed is not None:
        todos = [t for t in todos if t.get('completed') == filter_completed]
    
    return {
        'success': True,
        'count': len(todos),
        'todos': todos
    }


def update_todo(todo_id: int, description: Optional[str] = None, 
                completed: Optional[bool] = None, due_date: Optional[str] = None,
                priority: Optional[str] = None) -> Dict:
    """
    Update an existing todo item.
    
    Args:
        todo_id: The ID of the todo to update
        description: New description (optional)
        completed: New completion status (optional)
        due_date: New due date (optional)
        priority: New priority (optional)
    
    Returns:
        Dict with success status and updated todo
    """
    todos = load_todos()
    
    # Find the todo
    todo = None
    for t in todos:
        if t.get('id') == todo_id:
            todo = t
            break
    
    if not todo:
        return {
            'success': False,
            'message': f'Todo with ID {todo_id} not found'
        }
    
    # Update fields
    if description is not None:
        todo['description'] = description
    if completed is not None:
        todo['completed'] = completed
    if due_date is not None:
        todo['due_date'] = due_date
    if priority is not None:
        todo['priority'] = priority
    
    todo['updated_at'] = datetime.now().isoformat()
    
    save_todos(todos)
    
    return {
        'success': True,
        'message': f'Updated todo {todo_id}',
        'todo': todo
    }


def delete_todo(todo_id: int) -> Dict:
    """
    Delete a todo item.
    
    Args:
        todo_id: The ID of the todo to delete
    
    Returns:
        Dict with success status
    """
    todos = load_todos()
    
    # Find and remove the todo
    original_count = len(todos)
    todos = [t for t in todos if t.get('id') != todo_id]
    
    if len(todos) == original_count:
        return {
            'success': False,
            'message': f'Todo with ID {todo_id} not found'
        }
    
    save_todos(todos)
    
    return {
        'success': True,
        'message': f'Deleted todo {todo_id}'
    }


# ============================================================================
# Memory Management Functions
# ============================================================================

def load_memories() -> List[Dict]:
    """Load memories from file."""
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_memories(memories: List[Dict]) -> None:
    """Save memories to file."""
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memories, f, indent=2)


def save_memory(content: str, category: str = "general") -> Dict:
    """
    Save an important piece of information to memory.
    
    Args:
        content: The information to remember
        category: Category of memory (personal, preference, event, goal, etc.)
    
    Returns:
        Dict with success status
    """
    memories = load_memories()
    
    new_memory = {
        'id': max([m.get('id', 0) for m in memories], default=0) + 1,
        'content': content,
        'category': category,
        'timestamp': datetime.now().isoformat()
    }
    
    memories.append(new_memory)
    save_memories(memories)
    
    return {
        'success': True,
        'message': 'Memory saved',
        'memory': new_memory
    }


def recall_memory(query: Optional[str] = None, category: Optional[str] = None) -> Dict:
    """
    Recall memories, optionally filtered by query or category.
    
    Args:
        query: Search term to filter memories (searches in content)
        category: Filter by category
    
    Returns:
        Dict with success status and list of memories
    """
    memories = load_memories()
    
    # Filter by category
    if category:
        memories = [m for m in memories if m.get('category') == category]
    
    # Filter by query (simple substring search)
    if query:
        query_lower = query.lower()
        memories = [m for m in memories if query_lower in m.get('content', '').lower()]
    
    # Sort by timestamp (most recent first)
    memories.sort(key=lambda m: m.get('timestamp', ''), reverse=True)
    
    return {
        'success': True,
        'count': len(memories),
        'memories': memories
    }


# ============================================================================
# Tool Definitions for Function Calling
# ============================================================================

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "add_todo",
            "description": "Add a new todo item to the user's list",
            "parameters": {
                "type": "object",
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "The task description"
                    },
                    "due_date": {
                        "type": "string",
                        "description": "Optional due date in YYYY-MM-DD format"
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["low", "medium", "high"],
                        "description": "Priority level of the task"
                    }
                },
                "required": ["description"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_todos",
            "description": "List all todo items, optionally filtered by completion status",
            "parameters": {
                "type": "object",
                "properties": {
                    "filter_completed": {
                        "type": "boolean",
                        "description": "If true, show only completed todos. If false, show only incomplete. If omitted, show all."
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_todo",
            "description": "Update an existing todo item",
            "parameters": {
                "type": "object",
                "properties": {
                    "todo_id": {
                        "type": "integer",
                        "description": "The ID of the todo to update"
                    },
                    "description": {
                        "type": "string",
                        "description": "New description for the task"
                    },
                    "completed": {
                        "type": "boolean",
                        "description": "New completion status"
                    },
                    "due_date": {
                        "type": "string",
                        "description": "New due date in YYYY-MM-DD format"
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["low", "medium", "high"],
                        "description": "New priority level"
                    }
                },
                "required": ["todo_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_todo",
            "description": "Delete a todo item from the list",
            "parameters": {
                "type": "object",
                "properties": {
                    "todo_id": {
                        "type": "integer",
                        "description": "The ID of the todo to delete"
                    }
                },
                "required": ["todo_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "save_memory",
            "description": "Save an important piece of information to memory for future recall",
            "parameters": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The information to remember"
                    },
                    "category": {
                        "type": "string",
                        "enum": ["personal", "preference", "event", "goal", "general"],
                        "description": "Category of the memory"
                    }
                },
                "required": ["content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "recall_memory",
            "description": "Recall memories from past conversations",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search term to find relevant memories"
                    },
                    "category": {
                        "type": "string",
                        "enum": ["personal", "preference", "event", "goal", "general"],
                        "description": "Filter memories by category"
                    }
                }
            }
        }
    }
]


# Map function names to actual functions
FUNCTION_MAP = {
    "add_todo": add_todo,
    "list_todos": list_todos,
    "update_todo": update_todo,
    "delete_todo": delete_todo,
    "save_memory": save_memory,
    "recall_memory": recall_memory
}


def execute_function(function_name: str, arguments: Dict) -> Dict:
    """
    Execute a tool function by name with given arguments.
    
    Args:
        function_name: Name of the function to execute
        arguments: Dictionary of arguments to pass to the function
    
    Returns:
        Result from the function execution
    """
    if function_name not in FUNCTION_MAP:
        return {
            'success': False,
            'message': f'Unknown function: {function_name}'
        }
    
    try:
        func = FUNCTION_MAP[function_name]
        result = func(**arguments)
        return result
    except Exception as e:
        return {
            'success': False,
            'message': f'Error executing {function_name}: {str(e)}'
        }
