my_expense = [2200,2350,2600,2130,2190]
print(my_expense[1] - my_expense[0])
print(sum(my_expense[:3]))
print(2000 in my_expense)
my_expense.append(1980)
my_expense[-3] -= 200
print(my_expense)

heros = ['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
black_panther = heros.pop(-1)
print(heros)
heros.insert(3,black_panther)
print(heros)
heros[1:3]=['doctor strange']
print(sorted(heros))