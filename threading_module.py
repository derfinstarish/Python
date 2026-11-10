# import threading
# def add(a,b):
#     print(a+b)

# def sub(x,y):
#     print(x-y)

# a1=threading.Thread(target=add,args=(10,8))
# a2=threading.Thread(target=sub,args=(10,8))
# a1.start()
# a2.start()
# a1.join()
# a2.join()

#generator
# def seq(x):
#     for i in range(x):
#         yield i

# x=seq(5)
# print(next(x))
# print(next(x))
# print(next(x))

# practice threading

# import threading
# def add(a,b):
#     print(a+b)

# def sub(x,y):
#     print(x-y)

# def mul(m,n):
#     print(m*n)

# def div(p,q):
#     print(p/q)

# a1 =threading.Thread(target=add, args=(10, 8))
# a2 =threading.Thread(target=sub, args=(10, 8))
# a3 =threading.Thread(target=mul, args=(10, 2))
# a4 =threading.Thread(target=div, args=(10, 2))

# a1.start()
# a2.start()
# a3.start()
# a4.start()

# a1.join()
# a2.join()
# a3.join()
# a4.join()

#grenerator

def seq(x):
    for i in range(x):
        yield i
x = seq(11)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))