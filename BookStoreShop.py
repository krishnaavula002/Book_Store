# from utils import database
import BookStoreDatabase


User_choice = """
Enter :
'a' = to a add new book
'l' = to lits all books
'r' = to mark the book as read
'd' = to delet a book
'q' = to quit
"""


def menu():
    BookStoreDatabase.create_book_table()
    user_input = input(User_choice)
    while user_input !='q':
        if user_input =='a':
            prompt_add_book()
        elif user_input =='l':
            list_books()
        elif user_input =='r':
            prompt_raad_book()
        elif user_input =='d':
            prompt_delet_book()
        user_input =input(User_choice)


def prompt_add_book():
    name =input("enter the new book name : ")
    author =input("enter the new book author : ")

    BookStoreDatabase.insert_book(name,author)

def  list_books():
    for book in BookStoreDatabase.get_all_books():
        read = 'Yes' if book ['read'] else 'No'
        print(f"{book['name']} by {book['author']} — Read: {read}")

def  prompt_raad_book():
    name = input("Enter the name of the book you just finished reading: ")
    BookStoreDatabase.mark_book_as_read(name)

def  prompt_delet_book():
    name = input('Enter the name of the book you wish to delete ')
    BookStoreDatabase.delet_book(name)

menu()

