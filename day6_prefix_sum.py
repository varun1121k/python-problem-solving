# Day 6 - Prefix Sum

nums = [1, 2, 3, 4, 5]

prefix = [0] * len(nums)
prefix[0] = nums[0]

for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] + nums[i]

# Example query: sum from index 1 to 3
l, r = 1, 3

if l == 0:
    print(prefix[r])
else:
    print(prefix[r] - prefix[l-1])
