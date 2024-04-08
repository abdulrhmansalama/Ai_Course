import csv


class Book:
    def __init__(self , title, author , genre , publication_year):
        self.title=title
        self.author=author
        self.genre=genre
        self.publication_year=publication_year



class Library :
    def __init__(self):
        self.book_list=[]
        with open('books.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for book in reader:
                book=Book()
                book[0]=title
                book[1]=author
                book[2]=genre
                book[3]=publication_year                
        pass
    
    def add_book(self , book):
        self.book_list.append(book)
        with open('books.csv', 'w' , newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([book.title, book.author, book.genre ,  book.publication_year]) 
    def remove_book(self , book):
        self.book_list.remove(book)
        
    # def search(self , title ,author):
        
    
    def display(self ):
        for book in self.book_list :
            print(book.title)
            print(book.author)
            print(book.genre)
            print(book.publication_year)
            print("\n")
            

def interface ():
    book = book_list[]:
    while True:
        print("Welcome to the library!")
        print ("Please enter your choice ")
        print ("1.Add a new Book.")
        print ("2.Remove an existing Book.")
        print ("3.Search for a Book.")
        print ("4.Display all Books.")
        print ("5.Quit.")
        ch=input("Enter your choice : ")
        if ch=='1':
            b=Book()
            b.getdetails()
            lib.add_book(b)
        elif ch=='2':
            t=input("Enter Title of the book you want to delete : ")
            lib.remove_book(lib.search(t))
        elif ch=='3':    
            t=input("Enter Title of the book you are looking for : ")





        elif ch=='4':
            lib.display()
        elif ch=='5':
            break
        else:
            break
interface()
            

            
        
    
    
        