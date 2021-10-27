proceeds = int(input('Enter proceeds: '))
expenses = int(input('Enter expenses: '))
if expenses > proceeds:
    print("The company isn't profitable")
else:
    profit = proceeds - expenses
    print("The company is profitable. Profitability: ", profit / proceeds)
    employees = int(input('Enter number of employees: '))
    print("Profit per employee = ", profit / employees)