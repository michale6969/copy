class UndoRedoSystem:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
        self.document = ""

    def make_change(self, change):
        self.undo_stack.append(self.document)
        self.document = change
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()
        else:
            print("No actions to undo.")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.document)   
            self.document = self.redo_stack.pop()
        else:
            print("No actions to redo.")


editor = UndoRedoSystem()
print("Commands: 'change <text>', 'undo', 'redo', 'quit'")

while True:
    # 1. Print current state and get input on one line
    command_line = input(f"\nDoc: '{editor.document or 'Empty'}'\n> ").strip()

    if not command_line:
        continue
        
    # 2. Split the command from its text (if any)
    parts = command_line.split(maxsplit=1)
    command = parts[0].lower()

    # 3. Process the command
    if command == 'change':
        if len(parts) > 1:
            editor.make_change(parts[1]) # Use the text after 'change'
        else:
            print("Usage: change <your new text>")
            
    elif command == 'undo':
        editor.undo()
        
    elif command == 'redo':
        editor.redo()
        
    elif command == 'quit':
        print("Goodbye!")
        break # Exit the loop
        
    else:
        print("Unknown command. Try: 'change', 'undo', 'redo', or 'quit'")
