def fact(num):
    num1 = 1
    for i in range(1, num + 1):
        num1 *= i
        yield num1

n = 5
for index, num2 in enumerate(fact(n)):
    print(index + 1, num2)