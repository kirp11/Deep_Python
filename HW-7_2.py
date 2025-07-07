from functools import reduce
import random

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

# array = [6,5,4,3,2,1,0]
# array1= [61,5,4,83,2,10,0]
#
# def lst_without_min(min_el):
#
#
#
# print(list(map(lambda x: reduce(lambda x,y: min(x,y), lst_without_min()), array)))

#_______________________________________________ ГЕНЕРАТОРЫ


# 1.1

def five_generator():
    i = 5
    while True:
        yield i
        i += 5

gen = five_generator()
for i in range(10):
    print(next(gen), end =", ")


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


# 1.4
print()
def podstr_generator(value, lenght):
    i = 0
    while True:
        podstr = value[i:(i+lenght)]
        yield podstr
        i += 1

value= "abcdefg"
lenght = 3
gen_str = podstr_generator(value = value, lenght = lenght)
for _ in range(len(value) - lenght+1):
    print(next(gen_str), end =", ")

# 1.5
print()
def int_generator(A, B):
    i = A

    while True:
        yield i
        i += 2
A = 1
B = 10

gen_between = int_generator(A = A, B = B)
for i in range((B-A)//2+1):
    print(next(gen_between), end =", ")


# 1.6
print()
def hundred_generator():

    while True:
        i = random.randint(0, 100)
        yield i

generator_hundred = hundred_generator()
for i in range(10):
    print(next(generator_hundred), end =", ")


# 1.7   костыльно....
print()
def fibo_generator():
    i1 = 0
    i2 = 1

    while True:
        summ = i1 + i2
        if i1==0:
            print("0, ", end = "")
        yield summ
        i2 = i1
        i1 = summ

generator_fib = fibo_generator()
for i in range(10):
    print(next(generator_fib), end =", ")


# 2.10
print()
def day_generator():
    day = 1

    while True:
        value = "День " +str(day)
        yield value
        day += 1

generator_day = day_generator()
for i in range(10):
    print(next(generator_day), end =", ")
