# Day 4 - Missing Number

nums = [1, 2, 4, 5]
n = 5

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing number:", missing)
