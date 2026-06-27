"""
Day 1 Python Practice
Problem: Find numbers that appear only once in a list
"""

n = int(input("enter the number of values: "))
num = []

for i in range(n):
    value = int(input("enter the value: "))
    num.append(value)

freq = {}

for value in num:
    if value in freq:
        freq[value] += 1
    else:
        freq[value] = 1

print("numbers appearing only once:")

for x in freq:
    if freq[x] == 1:
        print(x)
