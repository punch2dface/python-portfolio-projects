# Dictionary Python

'''
What is a Dictionary?
- a data structure that stores key-value pairs.
- keys must be unique. 
- value can be anyting (int, string, list, another dictionary, etc.)
'''

# example
# name, age, city are keys
# Ben, 45, Los Angeles are values
person = {
    "name": "Ben",
    "age": 45,
    "city": "Los Angeles"
}

'''
Accessing and Changing Values
'''

# Accessing

print(person["name"]) # outputs the value in the 'name' key: Ben

# Changing

person["age"] = 29 # changes the value in the key, "age", to 29

# Add new Key

person["job"] = "QA Tester" # adds key, "job", and its value, "QA Tester", to the dictionary

'''
Looping through dictionaries
'''

# Keys

for key in person:
    print(key) # prints all keys
    
# Values

for value in person.values():
    print(value) # prints all values
    
# Keys + Values

for key, value in person.items():
    print(key, value) # prints the key and values
    
'''
Checking Membership
'''

# checks if the key, "age", is in the dictionary
if "age" in person:
    print("Age exists!") 


'''
Removing Items
'''

person.pop("city") # removes both key and its values.


