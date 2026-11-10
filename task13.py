# to find the power and square root by using threading by using math module

# import threading
# import math

# def power(a,b):
#     print(math.pow(a,b))

# def sqrt(a):
#     print(math.sqrt(a))

# a1 = threading.Thread(target=power, args=(2, 2))
# a2 = threading.Thread(target=sqrt, args=(4,))

# a1.start()
# a2.start()

# a1.join()
# a2.join()

# to find the power and Area of triangle by using threading by using without math module

# import threading

# def power(a,b):
#     print(a**b)

# def areaoftriangle(base,height):
#     print(base * height * 1/2)

# a1 = threading.Thread(target=power, args=(2, 3))
# a2 = threading.Thread(target=areaoftriangle, args=(5, 10))

# a1.start()
# a2.start()

# a1.join()
# a2.join()

# to print 1 to 10 prime numbers by using genertor

def prime():
    for num in range(1, 11):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num

x = prime()
print(next(x))
print(next(x)) 
print(next(x)) 
print(next(x)) 