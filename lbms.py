class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print("\nBook borrowed successfully!")
        else:
            print("\nSorry, this book is not available.")

    def return_book(self):
        if self.available == False:
            self.available = True
            print("\nBook returned successfully!")
        else:
            print("\nThis book was not borrowed.")

    def display_info(self):
        print("\nTitle:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        if self.available:
            print("Status: Available")
        else:
            print("Status: Unavailable")


# main program
books = []

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display All Books")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("\nInvalid input! Please enter a number.")
        continue

 # add book
    if choice == 1:
        print("\n--- Add Book ---")
        title = input("Enter title: ")
        author = input("Enter author: ")

        while True:
            try:
                year = int(input("Enter year: "))
                break
            except:
                print("Please enter a valid year.")

        b = Book(title, author, year)
        books.append(b)
        print("Book added!")

 # borrow book 
    elif choice == 2:
        available_books = [b for b in books if b.available == True]

        if len(available_books) == 0:
            print("\nNo available books to borrow.")
        else:
            print("\n--- Borrow Book ---")
            for i in range(len(available_books)):
                print(f"{i+1} - {available_books[i].title} | {available_books[i].author} | {available_books[i].year}")

            try:
                pick = int(input("Select book number: "))
                available_books[pick-1].borrow_book()
            except:
                print("\nInvalid selection.")

# return book
    elif choice == 3:
        borrowed_books = [b for b in books if b.available == False]

        if len(borrowed_books) == 0:
            print("\nNo borrowed books to return.")
        else:
            print("\n--- Return Book ---")
            for i in range(len(borrowed_books)):
                print(f"{i+1} - {borrowed_books[i].title} | {borrowed_books[i].author} | {borrowed_books[i].year}")

            try:
                pick = int(input("Select book number: "))
                borrowed_books[pick-1].return_book()
            except:
                print("\nInvalid selection.")

 # display all the books
    elif choice == 4:
        if len(books) == 0:
            print("\nNo books to display.")
        else:
            print("\n--- Book List ---")
            for b in books:
                b.display_info()

# exit bye
    elif choice == 5:
        print("\nThank you for visiting our library!")
        break

    else:
        print("\nPlease choose from 1 to 5.")
