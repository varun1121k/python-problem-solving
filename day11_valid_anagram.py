# Day 11 - Valid Anagram

s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print("Not anagram")
else:
    count = {}

    for c in s:
        count[c] = count.get(c, 0) + 1

    for c in t:
        if c not in count or count[c] == 0:
            print("Not anagram")
            break
        count[c] -= 1
    else:
        print("Anagram")
