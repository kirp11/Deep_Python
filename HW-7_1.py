
#1
def count_calls(func):
    n = 0
    def wrapper(*args, **kwargs):
        nonlocal n
        func(*args, **kwargs)
        n += 1
        print(f"Функция '{func.__name__}' вызвана {n} раз(а)")
    return wrapper


@count_calls
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")
greet("Мария")


#2

def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(types)):
                if isinstance(args[i], types[i]):
                    try:
                        return func(*args)
                    except:
                        print(f"TypeError: Неверный тип аргумента {args[i]}. Ожидался {type(types[i])}, получен {type(args[i])}")
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))     # 5
print(add(2, '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>

#3

def validate_range(min_value, max_value):
    def decorator(func):
        def wrapper(*args):
            for i in args:
                if i>=min_value and i <= max_value:
                    return func(*args)
                else:
                    print(f"ValueError: Аргумент 'value' имеет значение {i}, что выходит за пределы [{min_value}, {max_value}]")
        return wrapper
    return decorator


@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")

set_percentage(50)     # Вывод: Установлено значение: 50%
set_percentage(150)    # ValueError: Аргумент 'value' имеет значение 150, что выходит за пределы [0, 100]

#4

def trace(func):
    deep = 0
    def wrapper(args):
        nonlocal deep
        print("    "*deep + f"---> Вход в функцию {func.__name__} с аргументами ({args},), ...")
        deep+=1
        result = func(args)
        deep -= 1
        print("    "*deep + f"<--- Выход из функции {func.__name__} с результатом {result}")
        return result

    return wrapper


@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)


#5

def uppercase_result(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result,str):
            result = result.upper()
        return result
    return wrapper


@uppercase_result
def get_greeting(name):
    return f"Привет, {name}"

print(get_greeting("Алексей"))  # Вывод: ПРИВЕТ, АЛЕКСЕЙ

@uppercase_result
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))  # Вывод: 5



# 6

def call_limit(max_calls):
    value_call = 0
    def decorator(func):
        nonlocal value_call

        def wrapper(*args):
            nonlocal value_call
            value_call += 1
            if value_call <= max_calls:
                return func(*args)
            else:
                print("RuntimeError: Превышено максимальное количество вызовов функции")
        return wrapper
    return decorator


@call_limit(max_calls=3)
def print_message(msg):
    print(msg)

print_message("Первый вызов")    # Вывод: Первый вызов
print_message("Второй вызов")    # Вывод: Второй вызов
print_message("Третий вызов")    # Вывод: Третий вызов
print_message("Четвертый вызов") # RuntimeError: Превышено максимальное количество вызовов функции '