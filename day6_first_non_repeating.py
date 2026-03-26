# Day 6 - First Non-Repeating Character

s = input("Enter string: ")

freq = {}

for char in s:
    freq[char] = freq.get(char, 0) + 1

for char in s:
    if freq[char] == 1:
        print("First non-repeating:", char)
        break
