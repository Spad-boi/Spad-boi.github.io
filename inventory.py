import time

inventory = [
    {"id": "B001", "name": "Textbook Python Basics", "STATUS": "AVAILABLE"},
    {"id": "B002", "name": "Advanced Python Programming", "STATUS": "CHECKED OUT"},
    {"id": "B003", "name": "Data Science with Python", "STATUS": "AVALIABLE"},
]

def add():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    book_status = input("Enter Book Status (AVALIABLE/CHECKED OUT): ")
    new_book = {"id": book_id, "name": book_name, "STATUS": book_status.upper()}
    inventory.append(new_book)
    print(f"Book '{book_name}' added to inventory.")

def view():
    print("="*30)
    if not inventory:
        print("No books in inventory.")
        return
    for book in inventory:
        print(f"ID: {book['id']}, Name: {book['name']}| STATUS: {book['STATUS'].upper}")

def menu():
    while True:
        print("\n===============Inventory Menu:===============")
        print("1. Add Book")
        print("2. View Inventory")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            print("Exiting inventory menu.")
            break
        else:
            print("Invalid choice. Please try again.")

print("Welcome to the Book Inventory System")
time.sleep(1)
menu()
