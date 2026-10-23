# len()
text = "Hello, World!"
print(len(text))

# str()
number = 123
text_number = str(number)
print(text_number)

# upper()
text = "Hello, World!"
print(text.upper())

# lower()
text = "Hello, World!"
print(text.lower())

# capitalize()
text = "hello, world!"
print(text.capitalize())

# strip()
text = "   Hello, World!   "
print(text.strip())

# replace()
text = "Hello, World!"
print(text.replace("World", "Python"))

# split()
text = "Hello, World!"
print(text.split(","))

# join()
words = ["Hello", "Python"]
text = ", ".join(words)
print(text)

# find()
text = "Hello, World!"
print(text.find("World"))
print(text.find("Python"))

# count()
text = "Hello, World!"
print(text.count("o"))

#startswith()
text = "Hello, World!"
print(text.startswith("Hello"))

#endswith()
text = "Hello, World!"
print(text.endswith("World!"))

# isdigit()
text = "12345"
print(text.isdigit())

# isalpha()
text = "Hello"
print(text.isalpha())

#isupper()
text = "HELLO"
print(text.isupper())

# islower()
text = "hello"
print(text.islower())

# title()
text = "hello, world!"
print(text.title())

# zfill()
text = "42"
print(text.zfill(5))