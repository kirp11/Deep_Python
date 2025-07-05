from functools import reduce

# 1
array = ["1","40","1080"]

numbers = map(lambda x: int(x), array)
print(list(numbers))

# 2
array = [1, 2, 3, 4, 5, 6]

numbers = filter(lambda x: x%2==0, array)
print(list(numbers))

# 3
array = [1, 2, 3, 4]

numbers = map(lambda x: x**2, array)
print(list(numbers))

# 4
array = ["cat", "elephant", "dog", "tiger"]

numbers = filter(lambda x: len(x)>3, array)
print(list(numbers))

#5
array = [1, 2, 3, 4]

print(reduce(lambda x,y: x*y, array))

#6

array = ["hello", "world", "Python"]

numbers = map(lambda x: int(len(x)), array)
print(list(numbers))

#7

array = ["apple", "banana", "pear", "strawberry"]

print(reduce(lambda x,y: max(len(str(x)), len(str(y))), array))

#8
array = ["hello", "world"]
numbers = map(lambda x: x.upper(), array)
print(list(numbers))

#9

array = ["1", "2", "3", "4"]
print(list(filter(lambda x: x%2 == 0, (map(lambda x: int(x), array)))))

#10

array = [-2, 3, -4, 5, 6]
print(reduce(lambda x,y: x*y, list(filter(lambda x: x>0, array))))

#11
array = ["apple", "banana", "orange", "grape"]
print(list(map(lambda x: int(len(x)),filter(lambda x: x[0] in "aeiouy", array))))

#12

array = ["racecar", "hello", "level", "world"]
print(list(filter(lambda x: x[::-1]==x, map(lambda x: x[::-1], array))))