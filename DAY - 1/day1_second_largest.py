"""
Problem: Find the second largest number in a list
"""

n = int(input("enter the number of values: "))
num = []

for i in range(n):
    value = int(input("enter the value: "))
    num.append(value)

largest = num[0]
second_largest = float("-inf")

for value in num:
    if value > largest:
        second_largest = largest
        largest = value
    elif value != largest and value > second_largest:
        second_largest = value

print("second largest number:", second_largest)
