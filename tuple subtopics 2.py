#1️ Creating a List
numbers = [10, 20, 30, 40]
names = ["Sony", "Mounika"]
mixed = [10, "Python", True]

print(numbers)
print(names)
print(mixed)

#2️ Accessing Items
numbers = [10, 20, 30, 40]
print(numbers[0])   # 10
print(numbers[2])   # 30

#3️ Slicing a List
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]

#4️ List Functions
numbers = [10, 20, 30, 40]

numbers.append(50)      # add at end
numbers.insert(2, 25)   # add at index 2
numbers.remove(30)      # remove value 30
numbers.pop()           # remove last value
numbers.sort()          # sort list
numbers.reverse()       # reverse list

print(numbers)

#5️ Looping through a List
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)