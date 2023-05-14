import datetime
import sys
import requests

class Booxsfee:
    def __init__(self, name='default name', contact='default contact ', address='default address',email = 'default email'):
        self.name = name
        self.contact = contact
        self.address = address
        self.email = email

    def display(self):
        print(f"Name: {self.name}, Contact: {self.contact}, Address: {self.address}")

    def display_books(self):
        with open('booklist.txt', 'r') as file:
            content = file.read()
        print(content)

    def add_book(self):
        title = input("Name of the Book:")
        bookauthor = input("Author Name:")
        genre = input("Genre of book: ")
        now = datetime.datetime.now()
        add_book = f"Title: {title}, Author: {bookauthor}, Genre: {genre}, Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
        with open("booklist.txt", 'a') as file:
            file.write(add_book)

    def delete_book(self):
        book_title = input("Enter the title of the book to delete: ")
        with open('booklist.txt', 'r') as file:
            lines = file.readlines()
        with open('booklist.txt', 'w') as file:
            for line in lines:
                if not line.startswith(f"Title: {book_title},"):
                    file.write(line)

    def lend_book(self):
        book_title = input("Enter the book you want to lend: ")
        with open('booklist.txt', 'r') as file:
            lines = file.readlines()
        for line in lines:
            if line.startswith(f"Title: {book_title},"):
                # Book found, lend it
                borrower_name = input("Enter your name: ")
                borrow_date = datetime.datetime.now()
                return_date = borrow_date + datetime.timedelta(days=7)
                lend_info = f"Book: {book_title}, Borrower: {borrower_name}, Borrow Date: {borrow_date.strftime('%Y-%m-%d %H:%M:%S')}, Return Date: {return_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
                with open('booklender.txt', 'a') as file:
                    file.write(lend_info)
                print(f"Book {book_title} has been successfully lent to {borrower_name}.")
                break
        else:
            # Book not found
            print(f"Book {book_title} not found in the library.")
    def lender_details(self):
        with open("booklender.txt",'r') as file:
            content = file.read()
        print(content)

print("Welcome to Booxsfee library: ")
print("Press \n[1] For login [2] For Sign up [3] For quit")

while True:
    try:
        get_in = int(input())
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        continue

    if get_in == 3:
        sys.exit()

    if get_in == 2:
        name = input("Enter name: ")
        contact = input("Enter contact: ")
        address = input("Enter address: ")
        email = input("Email address ")
        Reader = Booxsfee(name, contact, address, email)

        # get the user's IP address
        response = requests.get('https://api.ipify.org?format=json')
        ip_address = response.json()['ip']

        # use the IP address to get the user's location
        response = requests.get(f'https://geolocation-db.com/json/{ip_address}')
        location = response.json()

        print(location)
        country_name = location['country_name']
        city = location['city']
        state = location['state']

        reader_info = f"Name: {name}, Contact: {contact}, Address: {address}, Country: {country_name}, City: {city}, State: {state}\n"
        print(reader_info)
        with open('reader.txt', 'a') as file:
            file.write(reader_info)
        with open('reader.txt') as file:
            content = file.read()
        print(content)

    if get_in == 1:
        name = input("Enter your name like: Mausam Gurung")
        Reader = Booxsfee()
        with open("reader.txt", "r") as file:
            for line in file:
                if name in line:
                    print("Logged in.")
                    break
            else:
                print("Name not found.")
                sys.exit()

    while True:
        print("Press \n[1] Display books [2] Add a book [3] Delete [4] Lend_book [5] Lender_details [6] Quit")
        try:
            option = int(input())
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue

        if option == 6:
            sys.exit()

        if option == 1:
            Reader.display_books()

        if option == 2:
            Reader.add_book()
        if option == 3:
            Reader.delete_book()
        if option == 4:
            Reader.lend_book()
        if option == 5:
            Reader.lender_details()
