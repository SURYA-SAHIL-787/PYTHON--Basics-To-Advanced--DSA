from abc import ABC, abstractmethod

class LibraryItem(ABC):
    item_count = 0

    def __init__(self, title):
        self.title = title
        LibraryItem.item_count += 1

    @abstractmethod
    def show_details(self):
        pass

class Book(LibraryItem):
    def show_details(self):
        return f"Book: {self.title}"

class Magazine(LibraryItem):
    def show_details(self):
        return f"Magazine: {self.title}"

class Newspaper(LibraryItem):
    def show_details(self):
        return f"Newspaper: {self.title}"

items = [Book("Python Basics"), Magazine("Science Today"), Newspaper("The Hindu")]

for item in items:
    print(item.show_details())

print("Total Items:", LibraryItem.item_count)
