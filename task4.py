# to print the number pattern from 1 to 10 by using range like star pattern

num = 1
for i in range(1, 5):
    for j in range(i):
        if num <= 10:
            print(num, end=" ")
            num += 1
    print()