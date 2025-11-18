import time

inventory = [
    {"id": "B001", "name": "Textbook Python Basics","Age restriction":"For all", "STATUS": "AVAILABLE"},
    {"id": "B002", "name": "Advanced Python Programming","Age restriction":"For all", "STATUS": "CHECKED OUT"},
    {"id": "B003", "name": "Data Science with Python","Age restriction":"For all", "STATUS": "AVALIABLE"},
]
def welcome():
    print("Welcome to the library system.")
    time.sleep(1)
    while True:
        choose = input("Please register or login to continue, or quit. (R/L/Q): ").upper()
        if choose == 'R':
            register()
            menu()
        elif choose == 'L':
            login()
            menu()
        elif choose == 'Q':
            print("Exiting the system. Bfnunchuck")
        else:
            print("Invalid choice. Exiting the system.")

def add():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    book_status = input("Enter Book Status (AVALIABLE/CHECKED OUT): ")
    book_age_restriction = input("Enter Age Restriction (For all/13+/15+/18+): ")
    new_book = {"id": book_id, "name": book_name, "STATUS": book_status.upper()}
    inventory.append(new_book)
    print(f"Book '{book_name}' added to inventory.")

def delete():
    book_id = input("Enter Book ID to delete: ")
    for book in inventory:
        if book['id'] == book_id:
            inventory.remove(book)
            print(f"Book ID '{book_id}' removed from inventory.")
            return
    print(f"Book ID '{book_id}' not found in inventory, try again later.")

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
        print("4. Renew Book")
        print("5. Detail Correction")
        print("6. Check Out Book")
        print("7. Delete Book")
        print("8. Sort Inventory by Book ID")
        print("9. Exit Inventory Menu")
        choice = input("Choose an option (1-9): ")
        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            book = search(None)
            if book:
                print(f"Book Found: ID: {book['id']}, Name: {book['name']}, STATUS: {book['STATUS']}")
            else:
                print("Book not found in inventory.")
        elif choice == '4':
            renew()
        elif choice == '5':
            detail_correction()
        elif choice == '6':
            check_out()
        elif choice == '7':
            delete()
        elif choice == '8':
            sort_inventory()
        elif choice == '9':
            print("Exiting inventory menu.")
            break
        else:
            print("Invalid choice. Please try again.")
        
def search(book_id):
    input_name = input("Enter Book Name to search: ")
    for book in inventory:
        if book['name'].lower() == input_name.lower():
            return book
    return None

def renew():
    book_id = input("Enter Book ID to renew: ")
    for book in inventory:
        if book['id'] == book_id:
            if book['STATUS'].upper() == "CHECKED OUT":
                book['STATUS'] = "RENEWED"
                print(f"Book ID '{book_id}' has been RENEWED.")
            else:
                print(f"Book ID '{book_id}' is already RENEWED.")
            return
    print(f"Book ID '{book_id}' not found in inventory.")

def detail_correction():
    book_id = input("Enter Book ID to correct details: ")
    for book in inventory:
        if book['id'] == book_id:
            new_name = input("Enter new Book Name: ")
            new_status = input("Enter new Book Status (AVALIABLE/CHECKED OUT/RENEWED): ")
            new_age_restriction = input("Enter new Age Restriction: ")
            book['name'] = new_name
            book['STATUS'] = new_status.upper()
            book['Age restriction'] = new_age_restriction
            print(f"Book ID '{book_id}' details updated.")
            return
    print(f"Book ID '{book_id}' not found in inventory.")

def check_out():
    book_id = input("Enter Book ID to check out: ")
    user_age = int(input("Enter your age: "))
    for book in inventory:
        if book['id'] == book_id:
            if book['STATUS'].upper() == "AVALIABLE":
                if book['Age restriction'] == "18+" and user_age < 18:
                    print(f"Book ID '{book_id}' is restricted to users under 18.")
                elif book['Age restriction'] == "13+" and user_age < 13:
                    print(f"Book ID '{book_id}' is restricted to users under 13.")
                elif book['Age restriction'] == "15+" and user_age < 15:
                    print(f"Book ID '{book_id}' is restricted to users under 15.")
                elif book['Age restriction'] == "For all":
                    book['STATUS'] = "CHECKED OUT"
                    print(f"Book ID '{book_id}' has been CHECKED OUT.")
            else:
                print(f"Book ID '{book_id}' is not available for check out.") or print(f"Book ID '{book_id}' is already {book['STATUS']}.")
            return
    print(f"Book ID '{book_id}' not found in inventory.")

def sort_inventory():
    inventory.sort(key=lambda x: x['id'])
    print("Inventory sorted by book id.")

def register():
    user_name = input("Enter your name to register: ")
    user_id = input("Create your user ID of 10 numbers:___-___-____ ")
    print(f"User '{user_name}' with ID '{user_id}' registered successfully.")
    print("Registered successful.")

def login():
    user_name = input("Enter your name to login: ")
    user_id = input("Enter your user ID: ")
    print(f"User '{user_name}' with ID '{user_id}' logged in successfully.")
    print("Login successful.")

welcome()
