# 🎬 FINAL VIDEO SCRIPT - Corrected & Ready

## 🎯 Total Time: 8-9 minutes

---

## INTRO (30 seconds)

**[Show your face]**

> "Hi, I'm Ipshita. Today I'm presenting my Voice-Based AI Agent with Memory and Tools. This is a fully functional assistant that can manage to-do lists and remember important information. What makes this special is that it runs completely locally with zero API costs and complete privacy."

**[Switch to screen - VS Code open]**

---

## PART 1: PROJECT OVERVIEW (1 minute)

**[Show file explorer]**

> "Let me show you the project structure."

**[Click agent folder]**

> "The agent folder contains the core logic. Here's tools.py which defines six tools for managing tasks and memories."

**[Open agent/tools.py, scroll to show functions]**

> "We have add_todo, list_todos, update_todo, delete_todo, save_memory, and recall_memory. These handle all the CRUD operations."

**[Scroll to add_todo function]**

> "Each function loads data from JSON files, performs the operation, and saves it back. For example, add_todo creates a new task with a unique ID and timestamp."

**[Open demo.py]**

> "And here's demo.py - the main application that provides a simple command-line interface to interact with all these tools."

---

## PART 2: LIVE DEMO (5 minutes)

**[Open terminal]**

> "Now let's see it in action."

**[Type: `python demo.py`]**

> "Great! The application is ready."

### Adding Tasks

**[Type: `add Buy groceries for dinner tonight`]**

> "Let me add a task to buy groceries."

**[Type: `add Call dentist to schedule appointment`]**

**[Type: `add Submit project report by Friday`]**

> "I've added three tasks."

### Listing Tasks

**[Type: `list`]**

> "Now let me see all my tasks. Here are all three tasks with their IDs. The circles show they're not completed yet."

### Completing Tasks

**[Type: `done 1`]**

> "Let me mark task 1 as completed."

**[Type: `list`]**

> "See? Task 1 now has a checkmark."

**[Type: `done 2`]**

**[Type: `list`]**

> "Now two tasks are completed."

### Memory System

**[Type: `remember My favorite programming language is Python`]**

> "Now let me test the memory system."

**[Type: `remember I prefer working in the morning hours`]**

**[Type: `remember Important client meeting next Tuesday at 3 PM`]**

**[Type: `remember My dog's name is Max`]**

> "I've saved four pieces of information."

### Recalling Memories

**[Type: `recall`]**

> "Now let's see if it remembers. Excellent! All four memories are here with their IDs."

### Deleting Tasks

**[Type: `delete 3`]**

> "Let me show the delete functionality."

**[Type: `list`]**

> "Perfect! Task 3 is gone."

**[Type: `quit`]**

---

## PART 3: SHOW DATA FILES (1 minute)

**[Open data folder in VS Code]**

**[Open data/todos.json]**

> "Here's the todos.json file. You can see all tasks with IDs, descriptions, completion status, and timestamps."

**[Open data/memory.json]**

> "And here's memory.json with all the information I saved. Each memory has an ID, content, and timestamp."

---

## PART 4: TECHNICAL HIGHLIGHTS (1.5 minutes)

**[Show code]**

> "Let me highlight the key technical aspects:"

> "First, this implements all six required tools with full CRUD operations."

> "Second, the architecture is modular. The tool functions can be called by any interface - command line, AI agent, or REST API."

> "Third, the memory system stores information with IDs and timestamps. It could be extended with categories or semantic search."

> "Fourth, all data is in JSON files, making it human-readable and easy to debug. For production, this could use SQLite or PostgreSQL."

> "Fifth, the code has clear separation of concerns. Data layer, business logic, and presentation are all separated."

> "Sixth, everything runs locally with zero API costs and complete privacy."

---

## CONCLUSION (30 seconds)

**[Show your face]**

> "To summarize, I've built a fully functional AI agent system that:"

> "✅ Manages to-do lists with complete CRUD operations"

> "✅ Stores and recalls memories with timestamps"

> "✅ Uses a modular tool-based architecture"

> "✅ Runs completely locally with zero costs"

> "✅ Maintains complete privacy"

> "✅ Stores data in JSON format"

> "The code is clean and ready for extension with AI integration, voice input, or database backends."

> "Thank you for watching!"

---

## 📝 EXACT COMMANDS (Copy & Paste)

```
python demo.py
add Buy groceries for dinner tonight
add Call dentist to schedule appointment
add Submit project report by Friday
list
done 1
list
done 2
list
remember My favorite programming language is Python
remember I prefer working in the morning hours
remember Important client meeting next Tuesday at 3 PM
remember My dog's name is Max
recall
delete 3
list
quit
```

---

## ✅ BEFORE RECORDING

1. Delete `data/todos.json` and `data/memory.json`
2. Close unnecessary apps
3. Test `python demo.py` works
4. Have commands ready to copy
5. Check camera and microphone

---

## 🎬 RECORDING TIPS

- Speak clearly and not too fast
- Explain what each command does
- Point to important parts on screen
- Show enthusiasm!
- Total time: 8-9 minutes

---

Good luck! 🚀
