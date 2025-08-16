class Library:

    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following book in our library: {self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booksList:
            print("Sorry, we do not have that book.")
        elif book in self.lendDict:
            print(f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user 
            print(
                "Lender-Book database has been updated. You can take the book now."
            )
    
    def addBook(self, book):
        self.booksList.append(book)
        print(f"{book} has been added to the book list.")

    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("That book wasn't borrowed from us.")


if __name__ == '__main__':
    books = Library(['Python',
                     'Rich Dad Poor Dad',
                     'Harry Potter',
                     'C++ Basics',
                     'Algorithms by CLRS'], "Let's Upskill")
    
    user_name = input("Well come to our library! Please enter your name: ")

    while True:
        print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:")

        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit")

        user_choice = input("Enter your choice to continue:")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please enter a vaild option.")
            continue
        
        if user_choice == '1':
            books.displayBooks()
        elif user_choice == "2":
            books = input("Enter the name of the book you want to lend:")
            books.lendBook(user_name, book)
        elif user_choice