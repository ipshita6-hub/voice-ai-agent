# 🎯 Demo Examples - Copy & Paste Ready!

## 📋 For `quick_start_simple.py` (Fast & Recommended)

### Example Session 1: Basic To-Do Management
```
add: Buy groceries for the week
add: Call dentist to schedule appointment
add: Finish project report by Friday
list
done: 1
list
```

**Expected Output:**
```
✅ Added: Buy groceries for the week
✅ Added: Call dentist to schedule appointment
✅ Added: Finish project report by Friday

📋 Your tasks (3):
  ○ 1. Buy groceries for the week
  ○ 2. Call dentist to schedule appointment
  ○ 3. Finish project report by Friday

✅ Marked task 1 as done!

📋 Your tasks (3):
  ✓ 1. Buy groceries for the week
  ○ 2. Call dentist to schedule appointment
  ○ 3. Finish project report by Friday
```

---

### Example Session 2: Memory System
```
remember: My favorite color is blue
remember: I love Italian food, especially pizza
remember: I have a dog named Max
remember: My birthday is in December
recall
```

**Expected Output:**
```
🧠 Remembered: My favorite color is blue
🧠 Remembered: I love Italian food, especially pizza
🧠 Remembered: I have a dog named Max
🧠 Remembered: My birthday is in December

🧠 Your memories (4):
  • My favorite color is blue
  • I love Italian food, especially pizza
  • I have a dog named Max
  • My birthday is in December
```

---

### Example Session 3: Complete Workflow
```
add: Prepare presentation slides
add: Review code changes
add: Send email to team
list
done: 2
remember: Important client meeting on Tuesday at 3 PM
remember: Need to follow up with Sarah about the project
list
recall
done: 1
done: 3
list
```

---

### Example Session 4: Multiple Tasks
```
add: Morning workout at 6 AM
add: Team standup meeting at 9 AM
add: Lunch with client at 12 PM
add: Code review session at 2 PM
add: Finish documentation by 5 PM
list
done: 1
done: 2
list
```

---

## 🤖 For `quick_start.py` (AI-Powered, Slower)

### Example Session 1: Natural Language
```
Add a task to buy groceries tomorrow
Add another task to call mom with high priority
What's on my to-do list?
Mark task 1 as completed
Show me only incomplete tasks
```

---

### Example Session 2: Conversational
```
I need to remember to buy milk
What do I need to do today?
I finished the first task
My favorite color is blue and I love pizza
What do you remember about my preferences?
```

---

### Example Session 3: Mixed Commands
```
Add a task to finish the report
I also need to schedule a dentist appointment
What's on my list?
The first one is done
Remember that I have a meeting next Tuesday at 3 PM
What meetings do I have coming up?
```

---

## 🎬 Perfect Demo Script (5 minutes)

### Part 1: Show To-Do Features (2 min)
```
add: Buy groceries for dinner
add: Call dentist for checkup
add: Submit project report
list
done: 1
list
```

**Say:** "As you can see, I can add tasks, list them, and mark them as complete. Each task gets a unique ID and timestamp."

---

### Part 2: Show Memory Features (2 min)
```
remember: My favorite programming language is Python
remember: I prefer working in the morning
remember: Important client meeting on Friday at 2 PM
recall
```

**Say:** "The memory system stores important information with categories and timestamps, making it easy to recall later."

---

### Part 3: Show Data Persistence (1 min)

**Open files in VS Code:**
- `data/todos.json` - Show the JSON structure
- `data/memory.json` - Show stored memories

**Say:** "All data is stored in human-readable JSON format, making it easy to debug and extend."

---

## 🎥 Video Demo Full Script

### Opening (30 sec)
**Say:** "Hi, I'm Ipshita. Today I'm demonstrating my Voice-Based AI Agent with Memory and Tools. This agent can manage to-do lists and remember important information, all running locally with zero API costs."

---

### Demo Part 1: Adding Tasks (1 min)
```
add: Buy groceries for the week
add: Call dentist to schedule appointment  
add: Finish project documentation
list
```

**Say:** "Let me start by adding some tasks. I'll add three different tasks - buying groceries, calling the dentist, and finishing documentation. Now let me list all tasks to see what we have."

---

### Demo Part 2: Completing Tasks (1 min)
```
done: 1
list
done: 2
list
```

**Say:** "Great! Now I'll mark the first task as completed. Notice how it shows with a checkmark. Let me complete another one. Perfect! Now we can see which tasks are done and which are still pending."

---

### Demo Part 3: Memory System (1.5 min)
```
remember: My favorite color is blue
remember: I love Italian food, especially pizza
remember: I have an important client meeting next Tuesday at 3 PM
remember: My dog's name is Max
recall
```

**Say:** "Now let's test the memory system. I'll tell the agent some personal information - my favorite color, food preferences, an upcoming meeting, and about my dog. Now when I recall, it shows everything I've told it. This is useful for maintaining context across conversations."

---

### Demo Part 4: Show the Code (1 min)

**Open in VS Code:**
- `agent/tools.py` - Scroll to TOOLS array

**Say:** "Here's how it works. I've defined six tools using function calling format: add_todo, list_todos, update_todo, delete_todo, save_memory, and recall_memory. Each tool has a clear description and parameters."

---

### Demo Part 5: Show Data Files (1 min)

**Open files:**
- `data/todos.json`

**Say:** "Here's the todos.json file. You can see each task has an ID, description, completion status, creation timestamp, and priority. The completed tasks are marked as true."

**Open:**
- `data/memory.json`

**Say:** "And here's the memory storage. Each memory has an ID, content, category, and timestamp. This makes it easy to search and filter memories later."

---

### Closing (30 sec)
**Say:** "So to summarize, I've built a fully functional AI agent that manages to-do lists with complete CRUD operations, stores and recalls memories, and runs completely locally using Ollama with zero API costs and complete privacy. The code is modular, well-documented, and ready for extension. Thank you for watching!"

---

## 🎯 Quick Test Commands (Copy All at Once)

### Test 1: Basic CRUD
```
add: Task one
add: Task two  
add: Task three
list
done: 1
done: 2
list
```

### Test 2: Memory
```
remember: Fact one
remember: Fact two
remember: Fact three
recall
```

### Test 3: Mixed
```
add: Important meeting
remember: Meeting is at 3 PM
list
recall
done: 1
list
```

---

## 💡 Pro Tips for Demo

### What to Say:
1. **When adding tasks:** "I'm using the add_todo tool which creates a new task with a unique ID and timestamp."

2. **When listing:** "The list_todos tool retrieves all tasks from the JSON storage and displays them with their status."

3. **When completing:** "The update_todo tool modifies the task's completed status to true."

4. **When saving memory:** "The save_memory tool stores information with categories for easy retrieval."

5. **When recalling:** "The recall_memory tool searches through stored memories and returns relevant information."

### What to Show:
- ✅ File structure in VS Code
- ✅ Running the application
- ✅ All CRUD operations
- ✅ Memory save and recall
- ✅ JSON data files
- ✅ Tool definitions in code

### What NOT to Do:
- ❌ Don't wait too long between commands
- ❌ Don't make typos (practice first!)
- ❌ Don't forget to show the data files
- ❌ Don't rush through explanations

---

## 🚀 Ready-to-Use Demo (Just Copy & Paste)

```
# Session Start
add: Buy groceries for dinner tonight
add: Call dentist to schedule annual checkup
add: Submit quarterly project report
add: Review pull requests from team
list
done: 1
done: 2
list
remember: My favorite programming language is Python
remember: I prefer working early morning hours
remember: Important client presentation on Friday at 2 PM
remember: Team lead meeting every Monday at 10 AM
recall
done: 3
list
recall
quit
```

**This complete session shows:**
- ✅ Adding 4 tasks
- ✅ Listing tasks
- ✅ Completing 3 tasks
- ✅ Saving 4 memories
- ✅ Recalling memories
- ✅ Final status check

**Total time: 3-4 minutes** ⏱️

---

## 📊 What Each Command Demonstrates

| Command | Feature Shown | Evaluation Criteria |
|---------|---------------|---------------------|
| `add:` | Create (CRUD) | Tool usage 25% |
| `list` | Read (CRUD) | Tool usage 25% |
| `done:` | Update (CRUD) | Tool usage 25% |
| `remember:` | Memory save | Memory 20% |
| `recall` | Memory recall | Memory 20% |

**All criteria covered!** ✅

---

## 🎬 Final Checklist

Before recording:
- [ ] Clear data files (delete todos.json and memory.json)
- [ ] Practice the commands 2-3 times
- [ ] Have this file open for reference
- [ ] Test your microphone and camera
- [ ] Close unnecessary applications
- [ ] Have VS Code open with project

During recording:
- [ ] Speak clearly and not too fast
- [ ] Explain what each command does
- [ ] Show enthusiasm!
- [ ] Point out the tool usage
- [ ] Highlight the local/free aspect

After recording:
- [ ] Watch it once to check quality
- [ ] Verify all features are shown
- [ ] Check audio is clear
- [ ] Upload to Google Drive
- [ ] Set sharing to "Anyone with link"

---

Good luck with your demo! 🎉
