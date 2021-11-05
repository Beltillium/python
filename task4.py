n = int(input('Enter a number: '))
a = 0
while n > 0:
    if n % 10 > a:
        a = n % 10
    n //= 10
print(a)
