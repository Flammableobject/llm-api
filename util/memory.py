# util/memory.py

class SlidingWindowMemory:
    def __init__(self, window_size=5):
        self.window_size = window_size  # Max messages to keep
        self.memory = []  # Stores conversation history

    def add_message(self, role, content):
        """Adds a message while maintaining the memory size limit."""
        self.memory.append({"role": role, "content": content})

        # Trim memory if exceeding window size
        if len(self.memory) > self.window_size:
            self.memory.pop(0)

    def get_memory(self):
        """Returns stored messages."""
        return self.memory

    def clear_memory(self):
        """Resets memory."""
        self.memory = []
