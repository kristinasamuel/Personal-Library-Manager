# A Personal Library Manager for Books helps you organize, track, and manage your book collection with features like adding, updating, removing, and searching for books.

import json

class booksCollection:
    """A class to manage a collection of books, allowing the user to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []   # Initialize the list to store book details
        self.storage_file = "books_data.json"    # File to store the book data
        self.read_from_file()    # Read books from the file when the application starts

    def read_from_file(self):
        """load saved books from JSON file into memory
        If the file doesn't exit or its corrupted, start with an empty list."""
        try:
           with open(self.storage_file,"r") as file:
              self.book_list = json.load(file)
        except(FileNotFoundError , json.JSONDecodeError):  # Handle missing or corrupt file
            self.book_list = []  # Start with an empty collection if the file is missing or corrupted.

    def save_to_file(self):
        """Store the current book collection to a JSON file  for permanet storage."""  
        with open(self.storage_file,"w") as file:
            json.dump(self.book_list,file,indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from user."""
        print("📖 Let's add a new book in collection!")
        book_title = input("Enter book title: ")   
        book_author = input("Enter author: ") 
        publish_year = input("Enter publication year: ")
        book_genre = input("Book genre: ")
        is_book_read = (
            input("Have you read this book? (yes/no)").strip().lower() == "yes"
        )
        # Create a dictionary for the new book and add it to the collection.
        new_book ={
            "title":book_title,
            "author":book_author,
            "year":publish_year,
            "genre":book_genre,
            "read": is_book_read
        }
        self.book_list.append(new_book)
        self.save_to_file()
        print("✅ Book added successfully! 📚\n")


    def delete_book(self):
        """Remove a book from the collection using its title."""
        print("🔴 Let's remove a book from your collection.")
        book_title = input("Enter the title of the book to remove: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)   # Remove the book from the collection
                self.save_to_file()
                print(f"✅ The book '{book_title}' was removed successfully!\n")
                return
            print(f"❌ Book titled '{book_title}' not found in your collection.\n")

    def find_book(self):
        """Search for books in the collection by title or author name. """
        print("🔍 Let's search for a book!")
        search_type = input("Searched by:\n1. Title\n2. Author\nEnter you choices: ")
        search_text = input("Enter search term: ").lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]        
        if found_books:
          print("🎯 Matching books found:")
          for index, book in enumerate(found_books,1):
              reading_status = "Read" if book["read"] else "Unread"
              print(
                  f"{index}.{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}"
              )  
        else:
            print("❌ No matching books found.\n")

    def update_book(self):
        """Modify the deatil of an existing book in the collection."""
        print("✏️ Let's update a book's details.")
        book_title = input("Enter the title of the book to update: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("leave blank to keep existing value.")
                book["title"] = input(f"New title({book["title"]}):") or book["title"]
                book["author"] = (
                    input(f"New author({book["author"]}):") or book["author"]

                )
                book["year"] = input(f"New year ({book["year"]}):") or book["year"]
                book["gebre"] = input(f"New genre ({book["genre"]}):") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no):").strip().lower()
                    == "yes"
                )
                self.save_to_file()
                print("✅ Book updated successfully.\n")
                return
        print(f"❌ Book titled '{book_title}' not found.\n")  


    def show_all_books(self):
        """"Display all books in the collection with their details. """
        if not self.book_list:
            print("📚 Your book collection is empty.\n")
            return
        print("📘 Here are all the books in your collection: ")
        for index,book in enumerate(self.book_list,1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
            f"{index},{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {reading_status}"
             )
        print()


    def show_reading_progress(self):
           """Calculate and display statistics about your reading progress."""
           total_books = len(self.book_list)   
           completed_books = sum(1 for book in self.book_list if book["read"])
           completion_rate = (
               (completed_books / total_books * 100 ) if  total_books > 0 else 0 
           )  
           print(f"📊 Total books in collection: {total_books}")
           print(f"📚 Redaing Progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True: 
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")        

            user_choice = input ("Please choose an option (1-7):")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("👋 Thank you for using the Book Collection Manager. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    book_manager = booksCollection() 
    book_manager.start_application()               



