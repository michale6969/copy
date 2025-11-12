from collections import deque

class EventSystem:
    def __init__(self):
        self.queue = deque()
        
    def add_event(self, event):
        self.queue.append(event)
        print(f"Event '{event}' added to the queue.")
        
    def process_next(self):
        if self.queue:
            event = self.queue.popleft()
            print(f"Processing event: {event}")
        else:
            print("No events to process.")
            
    def display_pending(self):
        if not self.queue:
            print("Pending Events: [Empty]")
        else:
            print("Pending Events:", list(self.queue))
        
    def cancel_event(self, event):
        try:
            self.queue.remove(event)
            print(f"Canceled event: {event}")
        except ValueError:
            print(f"Event '{event}' not found or already processed.")

# --- New Interactive Loop ---
es = EventSystem()
print("--- Event Processing System ---")
print("Commands: add <event>, process, display, cancel <event>, quit")

while True:
    # 1. Get command from user
    command_line = input("\nEnter command: ").strip()

    if not command_line:
        continue # Ask again if they just hit Enter
        
    # 2. Split command from argument (e.g., "add E1")
    parts = command_line.split(maxsplit=1)
    command = parts[0].lower()

    # 3. Process the command
    if command == 'add':
        if len(parts) > 1:
            event_name = parts[1]
            es.add_event(event_name)
        else:
            print("Usage: add <event_name>")
            
    elif command == 'process':
        es.process_next()
        
    elif command == 'display':
        es.display_pending()

    elif command == 'cancel':
        if len(parts) > 1:
            event_name = parts[1]
            es.cancel_event(event_name)
        else:
            print("Usage: cancel <event_name>")

    elif command == 'quit':
        print("Exiting system. Goodbye!")
        break # Exit the while loop
        
    else:
        print(f"Unknown command: '{command}'")
