n = int(input())
b = 0
a = 1

while n > 0:
    d = n % 10
    b += d
    a *= d
    n //= 10
print(b)
print(a)    
