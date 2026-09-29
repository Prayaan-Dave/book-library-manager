import json
import csv
import os

# File paths for storing books
JSON_FILE = 'library.json'
CSV_FILE = 'library.csv'

# Helper function: load books from JSON
def load_books():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    return []

# Helper function: save books to JSON
def save_books(books):
    with open(JSON_FILE, 'w') as f:
        json.dump(books, f, indent=4)

# Add a new book to the library
def add_book(title, author, year):
    books = load_books()
    book = {"Title": title, "Author": author, "Year": year}
    books.append(book)
    save_books(books)
    print(f"Book '{title}' added successfully!")

# View all books in the library
def view_books():
    books = load_books()
    if not books:
        print("No books in the library.")
        return
    print(f"{'Title':<30} {'Author':<20} {'Year':<6}")
    print("-"*60)
    for book in books:
        print(f"{book['Title']:<30} {book['Author']:<20} {book['Year']:<6}")

# Export books to CSV
def export_to_csv():
    books = load_books()
    if not books:
        print("No books to export.")
        return
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Title", "Author", "Year"])
        writer.writeheader()
        writer.writerows(books)
    print(f"Books exported to {CSV_FILE} successfully!")

# CLI Menu
def menu():
    while True:
        print(" Book Library Manager ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Export to CSV")
        print("4. Exit")
        choice = input("Enter an option: ")
        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            year = input("Enter year of publication: ").strip()
            add_book(title, author, year)
        elif choice == '2':
            view_books()
        elif choice == '3':
            export_to_csv()
        elif choice == '4':
            print("Exiting the library manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()