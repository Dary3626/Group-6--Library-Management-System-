# --------------------------------------------
# Library Management System (Fixed Version)
# --------------------------------------------

def show_books(library):
    """Display all books, their quantities, and who borrowed them."""
    print("\nLibrary Inventory")
    print("-" * 60)

    total_books = 0
    total_available = 0
    total_borrowed = 0

    for book, info in library.items():
        available = info['available']
        total = info['total']
        borrowed = total - available

        borrowers = []
        for name, qty in info['borrowers'].items():
            borrowers.append(f"{name} ({qty})")
        borrowers_list = ", ".join(borrowers) if borrowers else "None"

        print(f"{book}")
        print(f"  Total: {total} | Available: {available} | Borrowed: {borrowed}")
        print(f"  Borrowers: {borrowers_list}")
        print("-" * 60)

        total_books += total
        total_available += available
        total_borrowed += borrowed

    print(f"Total books: {total_books}")
    print(f"Available: {total_available}")
    print(f"Borrowed: {total_borrowed}")
    print("-" * 60)


def borrow_book(library):
    """Allow a user to borrow one or more copies."""
    name = input("Enter your name: ").strip()
    book = input("Enter the book title to borrow: ").strip()

    if book in library:
        info = library[book]
        if info['available'] > 0:
            try:
                qty = int(input(f"How many copies of '{book}' do you want to borrow? "))
                if qty <= 0:
                    print("Please enter a positive number.")
                    return
                if qty > info['available']:
                    print(f"Only {info['available']} copies are available.")
                    return

                info['available'] -= qty
                info['borrowers'][name] = info['borrowers'].get(name, 0) + qty
                print(f"{name}, you have borrowed {qty} copies of '{book}'.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print(f"Sorry, all copies of '{book}' are borrowed.")
    else:
        print("Book not found in the library.")


def return_book(library):
    """Allow a user to return one or more copies."""
    name = input("Enter your name: ").strip()
    book = input("Enter the book title to return: ").strip()

    if book in library:
        info = library[book]
        if name in info['borrowers']:
            borrowed_qty = info['borrowers'][name]
            print(f"You currently borrowed {borrowed_qty} copies of '{book}'.")

            try:
                qty = int(input("How many copies do you want to return? "))
                if qty <= 0:
                    print("Please enter a positive number.")
                    return
                if qty > borrowed_qty:
                    print(f"You can't return more than you borrowed ({borrowed_qty}).")
                    return

                info['available'] += qty
                if qty == borrowed_qty:
                    del info['borrowers'][name]
                else:
                    info['borrowers'][name] -= qty

                print(f"Thank you, {name}, for returning {qty} copies of '{book}'.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print(f"{name}, you didn't borrow '{book}'.")
    else:
        print("This book does not belong to our library.")


def main():
    """Main function to run the library system."""
    library = {
        "Harry Potter": {"total": 15, "available": 15, "borrowers": {}},
        "The Hobbit": {"total": 10, "available": 10, "borrowers": {}},
        "1984": {"total": 12, "available": 12, "borrowers": {}},
        "To Kill a Mockingbird": {"total": 8, "available": 8, "borrowers": {}},
        "The Great Gatsby": {"total": 5, "available": 5, "borrowers": {}}
    }

    print("Welcome to the Library Management System")

    while True:
        print("\nMain Menu:")
        print("1. Show Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_books(library)
        elif choice == "2":
            borrow_book(library)
        elif choice == "3":
            return_book(library)
        elif choice == "4":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()