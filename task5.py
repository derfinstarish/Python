# Print the first 10 numbers in the Fibonacci series.

a = 0
b = 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c