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

#13

array = [2, 3, 4, 5, 6]
def factorial(x):
    if x==0 or x==1:
        return x
    elif x>1:
        return x*(factorial(x-1))

print(reduce (lambda x,y: x*y, list(map(lambda x: factorial(x), filter(lambda x: x%2 == 0, array)))))


#14

array = ["hello", "world", "Python", "is", "great"]
print(reduce(lambda x,y: x+" "+y, list(map(lambda x: x.upper(), filter(lambda x: len(str(x))%2==0, array)))))

#15 СОРТИРОВКА

array = [6,5,4,3,2,1,0]
array1= [61,5,4,83,2,10,0]

print(list(map(lambda x: min(without_min_element(array)), array)))

#_______________________________________________ ГЕНЕРАТОРЫ


# 1.1

# def five_generator():
#     i = 5
#     while True:
#         yield i
#         i += 5
#
# gen = five_generator()
# for i in range(10):
#     print(next(gen), end =", ")


# 1.2
print()
def square_generator():
    i = 1
    while True:
        square = i ** 2
        yield square
        i += 1


gen_square = square_generator()
for i in range(10):
    print(next(gen_square), end =", ")


# 1.3
print()
def ignor_3_generator():
    i = 0
    while True:
        if i%3 !=0:
            yield i
        i += 1

gen_ignor = ignor_3_generator()
for i in range(10):
    print(next(gen_ignor), end =", ")