# to print output by using read method in file handlyng by using while loop
#read with while loop

a = open("starish.text", "r")
print("Successfully opened starish.text")
while True:
    line = a.readline()
    if not line:
        break
    print(line.strip())
a.close()