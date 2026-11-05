# public

# class employee:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(self.name)
#         emp = employee("John")
#         emp.display()
#         print(emp.name)  # Accessing public attribute directly

# protected (_)

# class employee:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age  # Protected attribute

#     class subemp(employee):
#         def show_age(self):
#             print(self._age)
#             emp = subemp("Ros", 30)
#             print(emp.name)
#             emp.show_age()   

# private (__)

# class employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age  # Private attribute

#     class subemp(employee):
#         def show_age(self):
#             print(self.__age)  # This will raise an AttributeError
#             emp = subemp("Ros", 30)
#             print(emp.name)
#             emp.show_age()