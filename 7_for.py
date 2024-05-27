result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count_heads = 0
for value in result:
    if value == 'heads':
         count_heads += 1
print(count_heads)

for num in range(1,10,2):
    print(num*num)

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)

star = ''
for i in range(1,6):
    star += '*'
    print(star)
    
for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)