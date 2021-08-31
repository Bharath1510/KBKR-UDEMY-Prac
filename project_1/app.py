import my_functions as func 
import os
func.print_options()
option = input("enter:")
books = []
while option !="x" and option !="X":
    if option =='1':
        books.append(func.create_book())
    elif option =='2':
        func.save_books(books)
    elif option =='3':
        books = func.load_books()
    elif option =='4':
        func.issue_book(books)
    elif option =='5':
        func.return_book(books)
    elif option =='6':
        func.update_book(books)
    elif option =='7':
        func.show_all_books(books)
    elif option =='8':
        func.show_book(books)
    else:
        print("The given command doesn't exist")
    input("press enter to continue")
    os.system("cls")
    func.print_options()
    option = input("enter:")



    
