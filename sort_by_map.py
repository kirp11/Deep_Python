from functools import reduce

#15 СОРТИРОВКА

array__1 = [6,5,4,3,2,1,8]
array__2= [61,5,4,83,2,10,0]

def array_without_min(lst, value):
    ind = lst.index(value)
    i = 1
    result = list(filter(lambda x: x > reduce(lambda x, y: min(x, y), lst), lst))
    if i < ind:
        while i < ind:
            result = list(filter(lambda x: x>reduce(lambda x,y: min(x,y), result), result))
            i += 1
    return result


array = array__1

print(list(map(lambda x: reduce(lambda x,y: min(x,y), array if x==array[0] else array_without_min(array, x)), array)))

array = array__2

print(list(map(lambda x: reduce(lambda x,y: min(x,y), array if x==array[0] else array_without_min(array, x)), array)))