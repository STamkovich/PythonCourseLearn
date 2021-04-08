# функции - это блок кода, либо  блок инструкций
# процесс создания функции называеться - обьявлением
# define в переводе как определять
def function1():  # обвляем фукцию
    print("hello1")
    print("hello2")


print("Hello from outside")

function1()  # вызываем функцию


def function2(x):  # x(аргумент) - входные данные для работы функции
    return 2 * x  # возвращаемое знаение


print(function2(4))


def sum_of_two_numbers(x, y):
    return x + y


e = sum_of_two_numbers(4, 5)
print(e)


def function5(some_argument):
    print(some_argument)
    print("argument")


function5(5)


def function6():
    return 5


function6()
a = function6()
print(a)


def function7(x):
    print(x)
    print("message")
    return 3 * x


a = function7(10)
print(a)
