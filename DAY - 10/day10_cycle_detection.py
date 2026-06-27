# Day 10 - Detect Cycle (Simulation)

nums = [1, 2, 3, 4, 5]

visited = set()

has_cycle = False

for num in nums:
    if num in visited:
        has_cycle = True
        break
    visited.add(num)

print("Cycle detected:", has_cycle)
