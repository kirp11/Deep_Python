

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

def type_check(tuple):
    def decorator(func):
        def wrapper(*args):
            for i in tuple:
                try:
                    func(*args)
                except TypeError:
                    print(f"Неверный тип аргумента {args[i]}. Ожидался {type(tuple[i])}, получен {type(args[i])}")

        return wrapper

tuple = (int, int)

@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))     # 5
print(add(2, '3'))   # TypeError: Неверный тип аргумента 'b'. Ожидался <class 'int'>, получен <class 'str'>