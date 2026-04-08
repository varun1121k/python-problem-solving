# Day 9 - Next Greater Element

nums = [2, 1, 2, 4, 3]
result = [-1] * len(nums)
stack = []

for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        index = stack.pop()
        result[index] = nums[i]
    
    stack.append(i)

print(result)
