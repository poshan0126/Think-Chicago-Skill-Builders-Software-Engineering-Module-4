
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def view_cart(self):
        return [item.display_info() for item in self.items]
