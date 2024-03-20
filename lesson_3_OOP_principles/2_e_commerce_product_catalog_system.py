class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}"

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        return f"{super().display_info()}, Author: {self.author}"

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        return f"{super().display_info()}, Specs: {self.specs}"

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        return f"{super().display_info()}, Size: {self.size}"

def main():
    # Create instances of each subclass
    my_book = Book("1", "Python Essentials", 29.99, "John Doe")
    my_electronic = Electronic("2", "Laptop", 20, "16GB RAM, 512GB SSD")
    my_clothing = Clothing("3", "T-Shirt", 30, "Medium")

    # Call display methods
    print(my_book.display_info())
    print(my_electronic.display_info())
    print(my_clothing.display_info())

if __name__ == "__main__":
    main()
