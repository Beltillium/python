from functools import reduce

nums = [a for a in range(100, 1001) if a % 2 == 0]
print(reduce(lambda a, b: a * b, nums))