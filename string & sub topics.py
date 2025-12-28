#1️ String Basics
name = "Sony Mounika"
print(name)

# 2️ String Length
name = "Sony Mounika"
print(len(name))

#3️Access Characters (Indexing)
name = "Python"
print(name[0])   # P
print(name[3])   # h

#4️ String Slicing(starting:to ending-1)
text = "Python Programming"
print(text[0:6])     # Python
print(text[7:18])    # Programming

#5 Common String Functions
text = " hello python "

print(text.upper())      # HELLO PYTHON
print(text.lower())      # hello python
print(text.strip())      # hello python(strip means removing the spaces from the beginning and end of the string))
print(text.replace("python", "world"))

#6️ Check Word in String
sentence = "I am learning python"

if "python" in sentence:
    print("Yes, python is present")