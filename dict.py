#Topic: Dictionaries

#A dictionary stores data as key–value pairs.

#Key → unique name

#Value → data assigned to that key

#It’s written using curly braces { }.
#1 Creating a Dictionary
student = {
    "name": "Sony Mounika",
    "age": 20,
    "branch": "ECE"
}

print(student)

2#2 Accessing Values
print(student["name"])    
print(student["age"])     

3#3 Adding / Updating Items
student["marks"] = 85     
student["age"] = 21        

print(student)

#4 Removing Items
student.pop("marks")       
del student["branch"]      

#5 Looping through Dictionary
student = {"name":"Sony","age":20}

for key in student:
    print(key, ":", student[key])

6# Dictionary Functions

#keys() → all keys

#values() → all values

#items() → all key-value pairs
print(student.keys())
print(student.values())
print(student.items())