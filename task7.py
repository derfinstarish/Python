# To check wheather a number is prime or not from user the user entered by using Functions

def primeCheck(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

num = int(input("Enter a number: "))
primeCheck(num)

#some of the prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31