
# Count positive, negative and zero numbers

n = int(input("Enter number of elements: "))
nums = []

for i in range(n):
    value = int(input("Enter value: "))
    nums.append(value)

positive = 0
negative = 0
zero = 0

for value in nums:
    if value > 0:
        positive += 1
    elif value < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
