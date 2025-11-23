# Exercise B - Word Frequency Counter

'''
Given this list:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

Create a dictionary called "counts" where:
- keys = each unique word
- values = how many times it appears

Expected output should be:
{"apple": 3, "banana": 2, "orange": 1}

'''

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

print(counts)