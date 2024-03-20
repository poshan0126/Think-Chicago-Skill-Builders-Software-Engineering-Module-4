
from book import Book
from user import User
from cart import ShoppingCart

def main():
    # Create a book
    book1 = Book("Python Essentials", "John Doe", 29.99, "In Stock")

    # Create a user
    user1 = User("johndoe", "password123")

    # Create a shopping cart and add a book to it
    cart1 = ShoppingCart()
    cart1.add_item(book1)

    # Display information
    print(user1.display_info())
    print(cart1.view_cart())

if __name__ == "__main__":
    main()
