# Exercise C - using **kwargs

'''
write a function called describe_person:

requirements:
- accept any number of keyword argumetns using **kwargs
- print each key/value pair in the format
    - key: value
'''

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Ben", age=28, city="LA")