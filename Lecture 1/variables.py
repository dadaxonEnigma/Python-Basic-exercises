# ---------- ссылка на обьъект 
# a = [1,2,3,4]
# b = a 
# print(b)
# b.append(5)
# print(b)

# -------- типизированный язык
# a = 5 
# print(type(a))
# a = 'str'
# print(type(a))
# b = '5' + 5
# print(b)

# ------- isinstance
# a = 5 ; b = 4.5
# print(isinstance(a, float))
# print(isinstance(a, (int, float)))

# -------- atributes, methods
# a = 'foo'
# print(dir(a))
# print(getattr(a, "replace"))

# ------- iter
# 1 method using like funct for checking iter
# def isiterable(obj):
#     try:
#         iter(obj)
#         return True
#     except TypeError:
#         return False
# print(isiterable(12))

# # 2 method for only check
# from collections.abc import Iterable
# print(isinstance('hello', Iterable))

# ------------------- iter iterable
# lst = [1,2,3,4,5]
# it = iter(lst)
# print(next(it))
# print(next(it))


#----------------------- изменяемые и неизменяемые объекты
# mutable = list, dict, set, user_classes (по умолчанию)
# immutable = int, float, str, tuple, frozenset
# a = 'Dadakhon'
# print(id(a))
# a = 'Turgunboev ' + a
# print(id(a))

# a = [1,2,3]
# print(id(a))
# a.append(4)
# print(id(a))


# ---------- string
# a = 'this is a string'
# a[10] = 'f'
# b = a.replace('string', "longer string")
# print(a)
# print(b)

# str = Unicode simbols
# s = "python"
# l = ['p','y','t','h','o','n']
# print(list(s))
# print("".join(l))