books =[]

def create_book_table():
    pass

def get_all_books():
    return books

def insert_book(name,author):
    books.append({"name":name,"author":author,"read":False})

def mark_book_as_read(name):
    for book in books:
        if book['name']==name:
            book['read']=True


def delet_book(name): 
    for book in books:
        if book['name']==name:
            books.remove(book)
