import re
#1

def reverse_generator(A, B):
        while True:
            yield B
            if B>=A:
                B-=1
            else:
                B+=1


A = 5
B = 41


gen_rev = reverse_generator(A=A, B=B)

for _ in range(abs(A-B)+1):
    print(next(gen_rev), end = ", ")

#2

def fib_dev5_generator():
    a = 0
    b = 1
    while True:
        fib_value = a + b
        if fib_value % 5 == 0:
            yield fib_value
        a = b
        b = fib_value

gen_fib_div5 = fib_dev5_generator()

for i in range(10):
    print(next(gen_fib_div5), end = ", ")


#3
def faktorial_generator():
    p = 1
    while True:

        def faktorial(n):
            factorial = n
            while n>1:
                factorial = factorial*(n-1)
                n-=1
            return factorial
        yield faktorial(p)
        p+=1

gen_faktorial = faktorial_generator()
for i in range(10):
    print(next(gen_faktorial), end = ", ")

#4

def alphabet_generator():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while True:
        for i in range(len(alphabet)):
            yield alphabet[i]

gen_alphabet = alphabet_generator()

for i in range(50):
    print(next(gen_alphabet), end = ", ")

#5

def unique_generator(str_):
    new_str = re.split(r'[,.\n ]+', str_)
    plus_list = []
    while True:
        for i in range(len(new_str)):
            if new_str[i] not in plus_list:
                yield new_str[i]
                plus_list.append(new_str[i])

stroka = "apple orange apple banana orange"

str_gen = unique_generator(stroka)

for i in range(len(stroka)):
    print(next(str_gen), end = ", ")

#6

def unique_generator_text(text, K):
    new_text = re.split(r'[,.\n ]+', text)

    def search_max(lst):
        max_el = lst[0]
        for j in range(1, len(lst)):
            if len(lst[j])> len(max_el):
                max_el = lst[j]
        return max_el

    while True:
        max_ = search_max(new_text)
        if len(max_) > K:

            yield max_
        new_text.remove(max_)


text_ = "Python is an amazing programming language"
K = 4

text_gen = unique_generator_text(text_, K)

for i in range(3):
    print(next(text_gen), end = ", ")