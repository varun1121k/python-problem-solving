# Day 6 - Power of Number

def power(x, n):
    if n == 0:
        return 1
    
    half = power(x, n // 2)
    
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

x = 2
n = 10

print(power(x, n))
