
#1
# def count_calls(func):
#     n = 0
#     def wrapper(*args, **kwargs):
#         nonlocal n
#         func(*args, **kwargs)
#         n += 1
#         print(f"Функция '{func.__name__}' вызвана {n} раз(а)")
#     return wrapper
#
#
# @count_calls
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Алексей")
# greet("Мария")


#2

# def type_check(*types):
#     def decorator(func):
#         def wrapper(*args):
#             for i in range(len(types)):
#                 if isinstance(args[i], types[i]):
#                     return func(*args)
#                 else:
#                     return f"TypeError: Неверный тип аргумента {args[i]}. Ожидался {type(types[i])}, получен {type(args[i])}"
#         return wrapper
#     return decorator
#
#
# @type_check(int, int)
# def add(a, b):
#     return a + b
#
# print(add(2, 3))     # 5
# print(add(2, '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>

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