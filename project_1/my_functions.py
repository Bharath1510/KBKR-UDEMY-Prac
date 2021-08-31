from book import Book
import json

def print_options():
    print('Press the required button:')
    print('1-create a new book')
    print('2-save books locally')
    print('3-load books from the disk')
    print('4-issue book')
    print('5-return book')
    print('6-update book')
    print('7-show all books')
    print('8-show book')
    

def input_book_info():
    id = input('ID: ')
    name = input('Name: ')
    description = input('Description: ')
    isbn = input('ISBN: ')
    page_count = int(input('Page count: '))
    issued = input('Issued:enter y/Y if True, anything else if False')
    issued = (issued=="y" or issued=="Y")
    author = input('Author: ')
    year = int(input('Year: ')) 
    return {
        'id':id,
        'name':name,
        'description':description,
        'isbn':isbn,
        'page_count':page_count,
        'issued':issued,
        'author':author,
        'year':year,
    }

def create_book():
    print("Please enter the book information")
    book_input = input_book_info()
    book = Book(book_input['id'],book_input['name'],book_input['description'],book_input['isbn'],
                book_input['page_count'],book_input['issued'],book_input['author'],book_input['year'])
    print(book.to_dict())
    return book

def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file = open("books.dat","w")
        file.write(json.dumps(json_books, indent=4))
        print("Books saved successfully")
    except:
        print("There is an error saving the book")
    
def load_books():
    try:
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj =  Book(book['id'],book['name'],book['description'],book['isbn'],
                            book['page_count'],book['issued'],book['author'],book['year'])
            books.append(new_obj)
        print("Successfully loaded books")
        return books
    except:
        print("the file doesn't exist or an error occured while loading" )

def find_book(books,id):
    for index,book in enumerate(books):
        if book.id == id:
            return index
    return None

def issue_book(books):
    id = input("enter the book ID: ")
    index = find_book(books,id)
    if index != None:
        books[index].issued = True
        print("Book successfully issued..")
    else:
        print("Couldn't find the book you are looking for..")

def return_book(books):
    id = input("enter the book ID: ")
    index = find_book(books,id)
    if index != None:
        books[index].issued = False
        print("Book successfully returned..")
    else:
        print("Couldn't find the book you are looking for..")

def update_book(books):
    id = input("enter the book ID: ")
    index = find_book(books,id)
    if index!= None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("book successfully updated...")
    else:
        print("book not found...")

def show_all_books(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id = input('please enter the id of the book you are looking for:')
    index = find_book(books,id)
    if index != None:
        print(books[index].to_dict())
    else:
        print('we could not find the book you are looking for...')
    


    


