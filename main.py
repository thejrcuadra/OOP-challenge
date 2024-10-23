class Book:
    # init constructor method to initialize attributes
    def __init__(self, title, author, pages, genre, read = False, purchases = 0):
        self._title = title
        self._author = author
        self._pages = pages
        self._genre = genre
        self._read = read
        self._purchases = purchases

    # returning book instance's description
    def description(self):
        return f"Title: {self._title}, Author: {self._author}, Pages: {self._pages}, Genre: {self._genre}"
    
    # setting read to True and displaying confirmation message
    def markAsRead(self):
        self._read = True
        print(f"{self._title} has been marked as read!")
        return self._read
    
class eBookReader:
    # init contructor method to initialize lists (data)
    def __init__(self):
        self._availableBooks = []
        self._purchasedBooks = []
        self._genres = []
        self._titlesBought = []

    # add a book to available books (already populated data)
    def addBook(self, book):
        if book not in self._availableBooks:
            self._availableBooks.append(book)
            print(f"{book._title} has been added to system.")
        else:
            print(f"{book._title} is already in the system.")

    # buying a book if not purchased, available, and exists
    def buyBook(self, bookName):
        for book in self._availableBooks:
            if book._title == bookName:
                self._purchasedBooks.append(book)
                if book._title+'\n' not in self._titlesBought:
                    self._titlesBought.append(book._title+'\n')
                    print(f"{book._title} has been successfully purchased!")
                book._purchases += 1
                return
        print(f"{bookName} is not available.")

    # displaying the description of books inside purchased books list
    def viewPurchasedBooks(self):
        if not self._purchasedBooks:
            print(f"There are no purchased books ... yet!")
        else:
            print(f"These are the purchased books: ")
            for book in self._purchasedBooks:
                print('\t'+book.description())

    # marking a book as read if there book is already purchased and not yet read
    def readPurchasedBook(self, bookName):
        if not self._purchasedBooks:
            print(f"There are no purchased books ... yet!")
        else:
            for book in self._purchasedBooks:
                if book._title == bookName:
                    if book._read == False:
                        book.markAsRead()
                    else:
                        print(f"{book._title} has already been read.")
                    return
            print(f"{bookName} is not purchased.")

    # view which genres are available for purhcase in the system
    def availableGenres(self):
        if not self._availableBooks:
            print(f"There are no books available ... yet!")
        else:
            print(f"These are the available genres: ")
            for book in self._availableBooks:
                if book._genre not in self._genres:
                    self._genres.append(book._genre)
            for genre in self._genres:
                print('\t'+genre)

    # filtering method by genre with user input
    def filterByGenres(self):
        # display available genres
        eBookReader.availableGenres(self)
        # filtering and user input
        print(f"Select a genre to filter. (Case sensitive)")
        userGenre = input(" >")
        if userGenre not in self._genres:
            print(f"{userGenre} is not available.")
        else:
            print(f"These are the available books with genre \"{userGenre}\"")
            for book in self._availableBooks:
                if book._genre == userGenre:
                    print('\t'+book.description())

    def trackBookPurchases(self):
        if not self._purchasedBooks:
            print("There are no books purchased ... yet!")
        else:
            # creating additional lists to track data
            titles = []
            purchases = []
            for book in self._purchasedBooks:
                if book._purchases not in purchases:
                    purchases.append(book._purchases)
                if book._title not in titles:
                    titles.append(book._title)
            print("These are the books that have been purchased: ")
            for i in range(len(titles)):
                print('\t'+f"{titles[i]} has been purchased {purchases[i]} time(s).")

    def topPurchasedBooks(self):
        if not self._purchasedBooks:
            print("There are no books purchased ... yet!")
        else:
            # creating additional list for data
            purchaseCount = []
            # track which title have already been used
            usedTitles = []
            for book in self._purchasedBooks:
                if book._title not in usedTitles:
                    usedTitles.append(book._title)
                    purchaseCount.append(book._purchases)
            topPurchases = list(purchaseCount)
            topTitles = list(usedTitles)
            for x in range(len(topPurchases)):
                maxIndex = x
                for y in range(x + 1, len(topPurchases)):
                    if topPurchases[y] > topPurchases[maxIndex]:
                        maxIndex = y
                topPurchases[x], topPurchases[maxIndex] = topPurchases[maxIndex], topPurchases[x]
                topTitles[x], topTitles[maxIndex] = topTitles[maxIndex], topTitles[x]
            # display top 3 books by sales
            print("The top 3 most purchased books are: ")
            print('\t'+f"1. {topTitles[0]}: {topPurchases[0]} buys.")
            print('\t'+f"2. {topTitles[1]}: {topPurchases[1]} buys.")
            print('\t'+f"3. {topTitles[2]}: {topPurchases[2]} buys.")

    def searchAuthor(self):
        print("Enter the author name to search for available books: (Case sensitive)")
        userAuthor = input(" >")
        # creating additional lists to perform linear search
        authors = []
        books = []
        # addition assignment variable in case the linear search does not find matching author names
        counter = 0
        if not self._availableBooks:
            print("There are no books available ... yet!")
        else:
            for book in self._availableBooks:
                authors.append(book._author)
                books.append(book._title)
            for i in range(len(authors)):
                if authors[i] == userAuthor:
                    print('\t'+f"{books[i]} by {authors[i]} is available!")
                    counter += 1
            if counter == 0:
                print(f"{userAuthor} does not have books available right now.")

    def searchByTitle(self):
        if not self._availableBooks:
            print("There are no available books ... yet!")
        else:
            print("Enter the book's title to search for availability: (Case sensitive)")
            userTitle = input(" >")
            # creating additional list to perform sorting and binary search
            titles = []
            for book in self._availableBooks:
                titles.append(book._title)
            # selection sorting 
            for x in range(len(titles)):
                maxIndex = x
                for y in range(x + 1, len(titles)):
                    if titles[y] < titles[maxIndex]:
                        maxIndex = y
                titles[x], titles[maxIndex] = titles[maxIndex], titles[x]
            # proof of successfull sorting
            # print(titles)
            # binary search
            min = 0
            max = len(titles) - 1 
            mid = 0
            while min <= max:
                mid = (min + max) // 2
                if titles[mid] == userTitle:
                    print('\t'+f"{titles[mid]} has been found and is available.")
                    return
                else:
                    if titles[mid] < userTitle:
                        min = mid + 1
                    else:
                        max = mid - 1
            print('\t'+f"{userTitle} is not available.")

    def saveToFile(self):
        file = open('Resources/purchasedBooks.txt', 'w')
        for book in self._purchasedBooks:
            if book._title not in self._titlesBought:
                file.write(f"{book._title}"+'\n')
                self._titlesBought.append(f"{book._title}")
        file.close()
        print("File has been successfully saved.")

    def loadFromFile(self):
        file = open('Resources/purchasedBooks.txt', 'r')
        loadedTitles = file.readlines()
        self._titlesBought = loadedTitles
        file.close()
        print("File has been successfully loaded.")

    
def main():
    # print() # differentiate betweeen two mains

    # singular instance of eBookReader class
    userOne = eBookReader()

    # adding Book instances (books) to userOne's simulation
    userOne.addBook(Book("Mansfield Park", "Jane Austen", "488", "Novel"))
    userOne.addBook(Book("The Jungle Book", "Rudyard Kipling", "277", "Fiction"))
    userOne.addBook(Book("Little Women", "Louisa May Alcott", "449", "Novel"))
    userOne.addBook(Book("The Phantom of the Opera", "Gaston Leroux", "360", "Novel"))
    userOne.addBook(Book("Snow Crash", "Neil Stephenson", "559", "Fiction"))

    # simulating user purchases
    for i in range(6):
        userOne.buyBook("Mansfield Park")
    for i in range(1):
        userOne.buyBook("Little Women")
    for i in range(3):
        userOne.buyBook("The Phantom of the Opera")
    for i in range(4):
        userOne.buyBook("The Jungle Book")
    for i in range(10):
        userOne.buyBook("Snow Crash")

    # simulating user actions
    userOne.loadFromFile()
    userOne.availableGenres()
    userOne.trackBookPurchases()
    userOne.topPurchasedBooks()
    userOne.filterByGenres()
    userOne.searchAuthor()
    userOne.searchByTitle()
    userOne.saveToFile()

if __name__ == "__main__":
    main()
