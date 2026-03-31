# Day 8 - Daily Temperatures

temps = [73,74,75,71,69,72,76,73]

result = [0] * len(temps)
stack = []

for i in range(len(temps)):
    while stack and temps[i] > temps[stack[-1]]:
        index = stack.pop()
        result[index] = i - index
    
    stack.append(i)

print(result)
