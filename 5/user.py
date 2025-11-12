class HashTableChaining:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
        
    def hash_function(self, key):
        return key % self.size
        
    def insert(self, key, value):
        idx = self.hash_function(key)
        # Check if key already exists to update it
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                print(f"Updated key {key}.")
                return
        # If not found, append the new key-value pair
        self.table[idx].append((key, value))
        print(f"Inserted ({key}, '{value}') at index {idx}.")
        
    def search(self, key):
        idx = self.hash_function(key)
        for k, v in self.table[idx]:
            if k == key:
                print(f"Found key {key}: Value is '{v}'")
                return v
        print(f"Key {key} not found.")
        return None
        
    def delete(self, key):
        idx = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                print(f"Deleted key {key} from index {idx}.")
                return True
        print(f"Key {key} not found, nothing to delete.")
        return False

    # Added a display method to see the table
    def display(self):
        print("\n--- Hash Table State ---")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
        print("------------------------")

# --- New Interactive Loop ---
ht = HashTableChaining()
print("--- Hash Table with Chaining ---")
print("Commands: insert <key> <value>, search <key>, delete <key>, display, quit")

while True:
    command_line = input("\nEnter command: ").strip()
    
    if not command_line:
        continue
        
    parts = command_line.split(maxsplit=2)
    command = parts[0].lower()
    
    try:
        if command == 'insert':
            if len(parts) == 3:
                key = int(parts[1])
                value = parts[2]
                ht.insert(key, value)
            else:
                print("Usage: insert <key_number> <value_string>")
                
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
