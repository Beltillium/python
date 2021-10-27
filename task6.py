a = int(input('Enter the result of the first day: '))
b = int(input('Enter the target: '))
last_attempt = 0
n = 1
while a < b:
    a *= 1.1
    n += 1
print(n)

