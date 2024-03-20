class BudgetCategory:
    def __init__(self, name, budget):
        self.__name = name
        self.__budget = budget
        self.__expenses = 0

    # Getter and setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    # Getter and setter for budget
    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        if budget >= 0:
            self.__budget = budget
        else:
            print("Budget cannot be negative.")

    # Method to add expense
    def add_expense(self, amount):
        if amount > 0 and amount <= (self.__budget - self.__expenses):
            self.__expenses += amount
        else:
            print("Invalid expense amount.")

    # Method to display budget details
    def display_category_summary(self):
        return f"Name: {self.__name}, Allocated Budget: {self.__budget}, Remaining Budget: {self.__budget - self.__expenses}"

def main():
    food = BudgetCategory("Food", 500)
    food.add_expense(100)
    print(food.display_category_summary())

if __name__ == "__main__":
    main()
