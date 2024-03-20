class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password 

    def display_info(self):
        return f"Username: {self.username}"
