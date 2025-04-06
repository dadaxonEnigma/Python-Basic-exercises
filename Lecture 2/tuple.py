# ------ tuple = одномерная неизменяемая последовательность объектов 
# tup = (4,5,6)
# print(tup)

# tup =4,5,6
# print(tup)

# -------- любую последовательность to tuple
# listt = [1,2,3,4,5]
# print(tuple(listt))
# string = 'Dadakhon'
# print(tuple(string))

# -------- indexing in tuple []
# tup = (1,2,3,4)
# print(tup[0])

# -------- nested tuples
# nested_tup = (4,5,6),(7,8)
# print(nested_tup)
# print(nested_tup[0])

#--------- mutable obj in tuple
# tup = tuple(['foo', [1,2], True])
# tup[2] = False
# tup[1].append(3)
# print(tup)

#-------- распаковка кортежей 
# tup = (4,5,6)
# a, b, c = tup
# print(a)
# print(b)
# print(c)

# tup = 4,5,(6,7)
# a, b, (c,d) = tup
# print(d)

# -------- обмен значений 
# a, b = 1,2
# tmp = a
# a = b
# b = tmp
# print(a)
# print(b)
# b,a = a,b
# print(a)
# print(b)

# ------- обход последовательностей tuple list
# seq = [(1,2,3), (4,5,6), (7,8,9)]
# for a, b, c in seq:
#     print(f'a = {a}, b = {b}, c = {c}')

# ------- отшепить немсколько элементов
# values = 1,2,3,4,5,6

# a, b, *_ = values
# print(a)
# print(b)
# print(_)