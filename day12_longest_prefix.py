# Day 12 - Longest Common Prefix

strs = ["flower", "flow", "flight"]

prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]

print("Prefix:", prefix)
