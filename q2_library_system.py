def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
    else:
        print(f"Cannot borrow Book {book_id}.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(
                f"ID: {book_id}, "
                f"Title: {title}, "
                f"Author: {author}, "
                f"Year: {year}"
            )


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Add Books
    add_book(catalog, 101, "Python Basics", "John Smith", 2020)
    add_book(catalog, 102, "Data Structures", "Alice Brown", 2021)
    add_book(catalog, 103, "Machine Learning", "Andrew Ng", 2022)
    add_book(catalog, 104, "Artificial Intelligence", "Russell", 2023)

    # Register Members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 1)  # duplicate

    print("Registered Members:", members)

    # Borrow Books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Return One Book
    return_book(borrowed_books, 101)

    # Show Available Books
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()