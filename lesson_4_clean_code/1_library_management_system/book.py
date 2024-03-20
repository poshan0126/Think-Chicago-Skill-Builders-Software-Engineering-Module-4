
class Book:
    def __init__(self, title, author, price, stock_status):
        self.title = title
        self.author = author
        self.price = price
        self.stock_status = stock_status

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, Stock Status: {self.stock_status}"
