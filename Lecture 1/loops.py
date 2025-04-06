print(range(10))
print(list(range(10)))
print(list(range(0,20, 2)))
print(list(range(5, 0, -1)))

seq = [1,2,3,4,5,6]
for i in range(len(seq)):
    print(f"element {i}: {seq[i]}")

for i,val in enumerate(seq):
    print(f'element {i+1}: {val}')
    
    