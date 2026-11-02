# by using oops get details from the user and display name,age of the user

class person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def display(self):
        print(f"Name: {self.name}.")
        print(f"Your are {self.age} years old.")


x = person()
x.display()