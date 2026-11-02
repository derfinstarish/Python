# class person:
#     def fun(self,name,age):
#         print(name)
#         print(age)

# a=person()
# a.fun('derfin',19)


# class bank:
#     def __init__(self):
#         print('default constructor')
# x=bank()


class bank:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
x=bank('anu',20)
x.display()

y=bank('derfin',19)
y.display()
