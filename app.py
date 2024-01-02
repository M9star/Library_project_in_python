''''

import datetime
import sys
import requests

from flask import Flask, render_template, request, redirect

# Booxsfee class implementation
# class Booxsfee:
#     def __init__(self, name='default name', contact='default contact ', address='default address',email = 'default email'):
#         self.name = name
#         self.contact = contact
#         self.address = address
#         self.email = email
#
#     def display(self):
#         print(f"Name: {self.name}, Contact: {self.contact}, Address: {self.address}")
#
#     def display_books(self):
#         with open('booklist.txt', 'r') as file:
#             content = file.read()
#         print(content)
#
#     def add_book(self):
#         title = input("Name of the Book:")
#         bookauthor = input("Author Name:")
#         genre = input("Genre of book: ")
#         now = datetime.datetime.now()
#         add_book = f"Title: {title}, Author: {bookauthor}, Genre: {genre}, Date: {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
#         with open("booklist.txt", 'a') as file:
#             file.write(add_book)
#
#     def delete_book(self):
#         book_title = input("Enter the title of the book to delete: ")
#         with open('booklist.txt', 'r') as file:
#             lines = file.readlines()
#         with open('booklist.txt', 'w') as file:
#             for line in lines:
#                 if not line.startswith(f"Title: {book_title},"):
#                     file.write(line)
#
#     def lend_book(self):
#         book_title = input("Enter the book you want to lend: ")
#         with open('booklist.txt', 'r') as file:
#             lines = file.readlines()
#         for line in lines:
#             if line.startswith(f"Title: {book_title},"):
#                 # Book found, lend it
#                 borrower_name = input("Enter your name: ")
#                 borrow_date = datetime.datetime.now()
#                 return_date = borrow_date + datetime.timedelta(days=7)
#                 lend_info = f"Book: {book_title}, Borrower: {borrower_name}, Borrow Date: {borrow_date.strftime('%Y-%m-%d %H:%M:%S')}, Return Date: {return_date.strftime('%Y-%m-%d %H:%M:%S')}\n"
#                 with open('booklender.txt', 'a') as file:
#                     file.write(lend_info)
#                 print(f"Book {book_title} has been successfully lent to {borrower_name}.")
#                 break
#         else:
#             # Book not found
#             print(f"Book {book_title} not found in the library.")
#     def lender_details(self):
#         with open("booklender.txt",'r') as file:
#             content = file.read()
#         print(content)

# Initialize Booxsfee instance
# Reader = None




app = Flask(__name__)

# Your Booxsfee class and functions go here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        # Add your login logic here
        # Example: Check if the name exists in the reader.txt file
        return redirect('/dashboard')  # Redirect to the dashboard page after login
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Add your signup logic here
        return redirect('/dashboard')  # Redirect to the dashboard page after signup
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    # Render the dashboard with the available options
    return render_template('dashboard.html')

# Define other routes for displaying books, adding books, deleting, lending, and lender details

if __name__ == '__main__':
    app.run(debug=True)
'''
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# ... (Your Booxsfee class and other code)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect('/dashboard')  # Redirect to the dashboard page after login
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic here
        return redirect('/dashboard')  # Redirect to the dashboard page after signup
    return render_template('signup.html')

# ... (Other routes and application logic)

if __name__ == '__main__':
    app.run(debug=True)
