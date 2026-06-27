# Day 5 - Subarray with Given Sum

nums = [1, 2, 3, 7, 5]
target = 12

current_sum = 0
start = 0

for end in range(len(nums)):
    current_sum += nums[end]

    while current_sum > target:
        current_sum -= nums[start]
        start += 1

    if current_sum == target:
        print("Subarray found:", nums[start:end+1])
        break
