"""Memory storage and retrieval system."""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class MemoryStore:
    """
    Simple memory storage system for the agent.
    
    This is a wrapper around the memory functions in agent/tools.py
    that provides additional utility methods.
    """
    
    def __init__(self, memory_file: str = "data/memory.json"):
        """
        Initialize memory store.
        
        Args:
            memory_file: Path to memory storage file
        """
        self.memory_file = memory_file
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Ensure the memory file and directory exist."""
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump([], f)
    
    def get_all_memories(self) -> List[Dict]:
        """
        Get all memories.
        
        Returns:
            List of all memory entries
        """
        with open(self.memory_file, 'r') as f:
            return json.load(f)
    
    def get_recent_memories(self, count: int = 5) -> List[Dict]:
        """
        Get the most recent memories.
        
        Args:
            count: Number of recent memories to retrieve
        
        Returns:
            List of recent memory entries
        """
        memories = self.get_all_memories()
        memories.sort(key=lambda m: m.get('timestamp', ''), reverse=True)
        return memories[:count]
    
    def search_memories(self, query: str) -> List[Dict]:
        """
        Search memories by content.
        
        Args:
            query: Search query
        
        Returns:
            List of matching memory entries
        """
        memories = self.get_all_memories()
        query_lower = query.lower()
        return [
            m for m in memories 
            if query_lower in m.get('content', '').lower()
        ]
    
    def get_memories_by_category(self, category: str) -> List[Dict]:
        """
        Get memories by category.
        
        Args:
            category: Memory category
        
        Returns:
            List of memory entries in the category
        """
        memories = self.get_all_memories()
        return [m for m in memories if m.get('category') == category]
    
    def clear_all_memories(self):
        """Clear all memories (use with caution!)."""
        with open(self.memory_file, 'w') as f:
            json.dump([], f)
        print("🗑️ All memories cleared")
    
    def export_memories(self, output_file: str):
        """
        Export memories to a file.
        
        Args:
            output_file: Path to output file
        """
        memories = self.get_all_memories()
        with open(output_file, 'w') as f:
            json.dump(memories, f, indent=2)
        print(f"💾 Memories exported to {output_file}")
    
    def get_memory_stats(self) -> Dict:
        """
        Get statistics about stored memories.
        
        Returns:
            Dictionary with memory statistics
        """
        memories = self.get_all_memories()
        
        categories = {}
        for memory in memories:
            cat = memory.get('category', 'unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        return {
            'total_memories': len(memories),
            'categories': categories,
            'oldest_memory': min([m.get('timestamp', '') for m in memories]) if memories else None,
            'newest_memory': max([m.get('timestamp', '') for m in memories]) if memories else None
        }
