"""This code implements an autonomous library system that enables students to independently 
issue and return books, eliminating the requirement for human librarian"""

import datetime

BOOKS_FILE = "list_of_books.txt"  # File containing the list of books
LIBRARY_NAME = "Thermodynamics"  # Name of the library

class Library:
    def __init__(self):
        self.books_detail = {}  # Dictionary to store list of the books
        self.load_books()  # Load books from the file

    def load_books(self):
        with open(BOOKS_FILE) as file:  # Open the file containing the list of books
            for ID, line in enumerate(file, start=200):  # Read each line in the file
                book_title = line.strip()  # Remove leading/trailing whitespaces from the book title
                self.books_detail[str(ID)] = {  # Create a dictionary entry for each book
                    "books_title": book_title,
                    "student_name": "",
                    "issue_date": "",
                    "status": "(Available)"
                }

    def display_books_name(self):
        print("Book ID\t\t\t\t\t\tTitle")  # Print the table headers
        for key, value in self.books_detail.items():  # Iterate over the books dictionary
            print(key, "\t", value["books_title"], "\t", value["status"])  # Print book ID, title, and status

    def issue_book(self):
        book_id = input("Enter book ID: ")  # Prompt the user to enter the book ID
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  # Get the current date and time
        if book_id in self.books_detail:  # Check if the book ID exists in the books dictionary
            book = self.books_detail[book_id]  # Get the book details
            if book["status"] != "available":  # Check if the book is already issued
                print(f"This book is already issued to {book['student_name']} on {book['issue_date']}")
            else:
                student_name = input("Enter your name: ")  # Prompt the user to enter their name
                book["student_name"] = student_name  # Assign the student name to the book
                book["issue_date"] = current_date  # Assign the current date as the issue date
                book["status"] = "Already issued"  # Update the book status
                print("Book issued successfully!")
        else:
            print("Book ID not found!")  # Display an error message if the book ID is not found

    def submit_book(self):
        book_id = input("Enter book's ID: ")  # Prompt the user to enter the book ID
        if book_id in self.books_detail:  # Check if the book ID exists in the books dictionary
            book = self.books_detail[book_id]  # Get the book details
            if book["status"] == "available":  # Check if the book is already available
                print("This book has not been issued. Please check book ID again.")
            else:
                book["student_name"] = ""  # Reset the student name for the book
                book["issue_date"] = ""  # Reset the issue date for the book
                book["status"] = "available"  # Update the book status to available
                print("Successfully updated!")
        else:
            print("Book ID not found!")  # Display an error message if the book ID is not found

try:
    library = Library()  # Create an instance of the Library class
    press_key_list = {  
        "S": "display book list",
        "I": "issue book",
        "R": "return book",
        "Q": "quit"
    }

    key_press = ""
    while key_press != "Q":  # Loop until the user chooses to quit
        print(f"\nWelcome to {LIBRARY_NAME} library")  # library welcome message
        for key, value in press_key_list.items():  # Iterate over the key mappings
            print(f"Press {key} to {value}")  # Print the available options
        key_press = input("Press key: ").upper()  # Prompt the user to enter a key (converted to uppercase)
        if key_press == "I":
            print("\nIssuing books")  # Display the issuing books message
            library.issue_book()  # Call the issue_book() method of the Library instance
        elif key_press == "S":
            print("\nShowing list of books")  # Display the showing list of books message
            library.display_books_name()  # Call the display_books_name() method of the Library instance
        elif key_press == "R":
            print("\nSubmitting books")  # Display the submitting books message
            library.submit_book()  # Call the submit_book() method of the Library instance
        elif key_press == "Q":
            break  # Exit the loop if the user chooses to quit
        else:
            print("Invalid input. Please try again.")  # Display an error message for invalid input
except Exception as e:
    print("An error occurred:", str(e))  # Display an error message if an exception occurs


