# Day 3 - Binary Search

nums = [2, 4, 6, 8, 10, 12]
target = 10

low = 0
high = len(nums) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print("Element found at index", mid)
        found = True
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")
