# Exercise B Python

'''
Let the user manage a shopping list.
- start with an empty list
- let the user repeatedly enter items.
- typing "done" ends input.
- print:
    - the number of items
    - the list sorted alphabetically
    - the first and last item
'''

item_list = []

while True:
    user_input = (str(input("Enter item (or 'done'): ")))
    
    if user_input.lower() == 'done':
        break
    else:
        item_list.append(user_input)

print("You entered ", len(item_list), " items.")
sorted_list = sorted(item_list)
print("Sorted list: ", sorted_list)
print("First item: ", sorted_list[0])
print("Last item: ", sorted_list[-1])