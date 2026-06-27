# Day 6 - Valid Parentheses

s = input("Enter string: ")

stack = []
mapping = {')': '(', '}': '{', ']': '['}

valid = True

for char in s:
    if char in "({[":
        stack.append(char)
    else:
        if not stack or stack[-1] != mapping[char]:
            valid = False
            break
        stack.pop()

if valid and not stack:
    print("Valid")
else:
    print("Invalid")
