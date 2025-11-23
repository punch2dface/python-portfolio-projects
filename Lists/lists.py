# Lists Python

'''
Lists
- ordered, changeable collections
- can hold mixed types
- defined with []

Basic Operations
- access via index: my_list[0]
- slice: my_list[1:4]
- modify: my_list[2] = "hello

Add & Remove
- append()
- insert()
- remove()
- pop()

Looping
- for item in my_list:

Built-In Function
- len()
- sum()
- min(), max()
- sorted()

List Comprehensions
- Short way of building lists:
- squares = [x*x for x in range(10)]
'''

# Guided Practice

# Create and Access
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # outputs: apple
print(fruits[-1])   # outputs: cherry

# Modify
fruits[1] = "blueberry" # modifies fruits[1] value (banana) to blueberry
print(fruits) # outputs ["apple", "blueberry", "cherry"]

# Add/Remove
fruits.append("dragon fruit") # adds dragon fruit to the end of the list
fruits.insert(1, "mango")   # adds mango in fruits[1] where blueberry was and pushes everything that was at 1 and beyond further down the list
fruits.remove("cherry") # specifically remove an item
popped = fruits.pop() # removes last item in list
print(fruits)
print("Popped: ", popped)

# Iterate
for f in fruits:
    print(f)
    
# List Comprehension
numbers = [1, 2, 3, 4, 5]
squared = [n ** 2 for n in numbers] # the loop squares each item in the numbers list.
print(squared)