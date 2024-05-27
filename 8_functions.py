def get_area(base,height):
    return (1/2)*base*height
area = get_area(52,25)
print(area)

def get_areas(base,height,form = "triangle"):
    if form == 'rectangle':
        return base*height
    if form == 'triangle':
        return (1/2)*base*height

res = get_areas(52,25,'rectangle')
print(res)

count = int(input('Shape of count:'))
def shape(count):
    res=''
    for i in range(count):
        res += '*'
        print(res)
    return res
result = shape(count)
