# Exercise A - Basic List Manipulation

'''
1. Asks the user to enter 5 numbers
2. Stores them in a list.
3. Prints:
    - the list
    - the sum of the number
    - the smallest number
    - the numbers sorted
'''

num_list = []
for i in range(5):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))
            num_list.append(num)
            break
        except ValueError:
            print("Please enter a valid number.")
    
print("Numbers:", num_list)
print("Sum:", sum(num_list))
print("Smallest:", min(num_list))
print("Sorted:", sorted(num_list))

