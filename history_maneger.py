class HistoryManager:
    """Handles reading and writing calculation history to a file."""

    def __init__(self, filepath='history.txt'):
        self.filepath = filepath

    def save(self, expression, result):
        """Append one entry to the history file."""
        # TODO: Task 3 — implement this method
        def save(self, expression, result):
            with open(self.filepath, 'a') as file:
                file.write(f"{expression} = {result}\n")

    def load(self):
        """Read all lines from the history file. Return empty list if file not found."""
        # TODO: Task 4 — implement this method
        def load(self):
            try:
                with open(self.filepath, 'r') as file:
                    return file.readlines()
            except FileNotFoundError:
                return []

    def clear(self):
        """Erase all content from the history file."""
        # TODO: Bonus — implement this method
        def clear(self):
            with open(self.filepath, 'w') as file:
                pass