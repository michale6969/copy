from collections import Counter

borrow_records = {}

while True:
    try:
        num_books = int(input("Enter the number of books to record borrowings for: "))
        if num_books > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


for i in range(num_books):
    print(f"\nRecording data for Book {i + 1}:")
    book_name = input("Enter the book name: ")

    while True:
        try:
            borrow_count = int(input("Enter the number of times the book has been borrowed: "))
            if borrow_count >= 0:
                break
            else:
                print("Please enter a non-negative integer.")
        except ValueError: 
            print("Invalid input. Please enter a valid integer.")

    borrow_records[book_name] = borrow_count    

print("\n--- All Records Entered ---")
print(borrow_records)

if borrow_records:
    # 1. Average
    avg_borrowed = sum(borrow_records.values()) / len(borrow_records)

    # 2. Max and Min
    max_borrow = max(borrow_records.values())
    min_borrow = min(borrow_records.values())
    max_borrow_books = [book for book, count in borrow_records.items() if count == max_borrow]
    min_borrow_books = [book for book, count in borrow_records.items() if count == min_borrow]

    # 3. Zero borrow count
    zero_borrow_count = sum(1 for count in borrow_records.values() if count == 0)

    # 4. Mode borrow count
    mode_borrow = Counter(borrow_records.values()).most_common(1)[0][0]
    
    
    print(f"Average books borrowed: {avg_borrowed}")
    print(f"Highest borrowed books: {max_borrow_books} with {max_borrow} borrowings")
    print(f"Lowest borrowed books: {min_borrow_books} with {min_borrow} borrowings")
    print(f"Members with zero borrowings: {zero_borrow_count}")
    print(f"Most frequently borrowed book count (mode): {mode_borrow}")
else:
    print("No records were entered, no statistics to calculate.")
