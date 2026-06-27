# Day 8 - Find All Anagrams in a String

s = "cbaebabacd"
p = "abc"

from collections import Counter

p_count = Counter(p)
window = Counter()

result = []
k = len(p)

for i in range(len(s)):
    window[s[i]] += 1
    
    if i >= k:
        if window[s[i-k]] == 1:
            del window[s[i-k]]
        else:
            window[s[i-k]] -= 1
    
    if window == p_count:
        result.append(i - k + 1)

print(result)
