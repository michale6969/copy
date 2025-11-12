class HashTableLinearProbing:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.deleted = object()  # Special marker for deleted entries

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        idx = self.hash_function(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None or self.table[probe] == self.deleted:
                self.table[probe] = key
                print(f"Inserted key {key} at index {probe}.")
                return
            elif self.table[probe] == key:
                print(f"Key {key} already exists.")
                return
        print("Hash table is full. Could not insert key {key}.")

    def search(self, key):
        idx = self.hash_function(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                print(f"Search: Key {key} not found (chain broken).")
                return False
            if self.table[probe] == key:
                print(f"Search: Key {key} found at index {probe}.")
                return True
        print(f"Search: Key {key} not found (table searched).")
        return False

    def delete(self, key):
        idx = self.hash_function(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                print(f"Delete: Key {key} not found (chain broken).")
                return False
            if self.table[probe] == key:
                self.table[probe] = self.deleted
                print(f"Delete: Key {key} marked as deleted at index {probe}.")
                return True
        print(f"Delete: Key {key} not found (table searched).")
        return False

    def display(self):
        # Display the table contents, showing 'DEL' for deleted slots
        print("\n--- Hash Table State ---")
        print([
            'DEL' if x == self.deleted else x
            for x in self.table
        ])
        print("------------------------")

# --- New Interactive Loop ---
ht = HashTableLinearProbing()
print("--- Hash Table with Linear Probing ---")
print("Commands: insert <key>, search <key>, delete <key>, display, quit")

while True:
    command_line = input("\nEnter command: ").strip()
    
    if not command_line:
        continue
        
    parts = command_line.split(maxsplit=1)
    command = parts[0].lower()
    
    try:
        if command == 'insert':
            if len(parts) == 2:
                key = int(parts[1])
                ht.insert(key)
            else:
                print("Usage: insert <key_number>")
                
        elif command == 'search':
            if len(parts) == 2:
                key = int(parts[1])
                ht.search(key)
            else:
                print("Usage: search <key_number>")

        elif command == 'delete':
            if len(parts) == 2:
                key = int(parts[1])
                ht.delete(key)
            else:
                print("Usage: delete <key_number>")
                
        elif command == 'display':
            ht.display()
            
        elif command == 'quit':
            print("Goodbye!")
            break
            
        else:
            print(f"Unknown command: '{command}'")
            
    except ValueError:
        print("Error: The key must be an integer.")
