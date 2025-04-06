# a_list = [2,3,4,5,None]
# tup = ('foo','bar','baz')
# b_list = list(tup)
# print(b_list)
# b_list[1] = 'peekaboo'
# print(b_list)

# --------- добавление и удаление элементов 
# b_list = ['foo', 'bar','peekabo','baz']
# b_list.append('dwarf')
# print(b_list)

# b_list.insert(1, 'red')
# print(b_list)

#--------- collections.deque
# from collections import deque
# d = deque([1,2,3,4])
# d.append(5)
# d.appendleft(0)
# print(d)

#---------- pop 
# print(b_list)
# b_list.pop(2)
# print(b_list)

#------ Конкатенация и комбинирование списков
# a = [1,2,3,None]
# b = [5,6,7,True]
# print(a + b)
# 2 способ и лучше
# ls = [['Bar'],['Red'],['Baz']]
# everything = []
# for chunk in ls:
#     everything.extend(chunk)
# print(everything)

# --------- Сортировка + key=len
# a = [7,2,5,1,3]
# a.sort()
# print(a)

# b = ['saw', 'small','He','foxes','six']
# b.sort(key=len)
# print(b)

#------------- Вырезание 
# seq = [1,2,3,4,5,6,7,8,9]
# print(seq[1:5])

# seq[3:5] = [6,5,5,7]
# print(seq)

# print(seq[:-4])
# print(seq[-4:])
# print(seq[-6:-2])
# print(seq[::2])
# print(seq[::-1])
