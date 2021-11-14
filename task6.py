from itertools import cycle, count

n = 10
nums = [a for a in range(5)]
num_cycle = cycle(nums)
counter = count()
print([next(counter) for a in range(n)])
print([next(num_cycle) for a in range(n)])
