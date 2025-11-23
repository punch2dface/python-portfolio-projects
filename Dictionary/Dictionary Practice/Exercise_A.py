# Exercise A - Favorite Foods Dictionary

'''
Create a dictionary called favorite_foods where:
- keys = names of 3 people
- values = their favorite food

Print all names(keys)
Print all favorite foods(values)
Print each person and their food in a loop
Add a new person
Change one person's favorite food
'''

favorite_foods = {
    "todd": "tacos",
    "billy": "burgers", 
    "simon": "salad"
}

# Print all names(keys)
for name in favorite_foods:
    print(name)
    
# Print all favorite foods(values)
for food in favorite_foods.values():
    print(food)
    
# Print each person and their food in a loop
for name, food in favorite_foods.items():
    print(name, food)

# Add a person
favorite_foods["susan"] = "soup"

# Change one person's favorite food
favorite_foods["billy"] = "bacon"
