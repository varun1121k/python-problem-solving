# Day 4 - Find Duplicates

nums = [1, 2, 3, 2, 4, 1]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))
