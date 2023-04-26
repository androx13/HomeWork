"""
Завдання 2

Створіть програму, яка перевіряє, чи є паліндромом введена фраза.
"""


def check_phrase(palindrome):
    """

    :param palindrome:
    :return:
    """
    palindrome = phrase.lower().replace(" ", "")
    reverse_palindrome = palindrome[::-1]
    return palindrome == reverse_palindrome


print("Проверяем является ли фраза полиндромом(для выхода напишите 'exit' ")
while True:
    phrase = input("Введите фразу: ")
    if phrase == "exit":
        break
    if check_phrase(phrase):
        print(f"'{phrase}' - палиндром")
    else:
        print(f"'{phrase} - не палидром'")


"""
Завдання 3

Нехай на кожну сходинку можна стати з попередньої або переступивши через одну.
Визначте, скількома способами можна піднятися на задану сходинку.
"""


def possible_ways(ways):
    if ways <= 1:
        return 1
    else:
        return possible_ways(ways - 1) + possible_ways(ways - 2)


step = int(input("Введите ступеньку: "))
print(f"Количество способов подняться на ступеньку {step}: {possible_ways(step)}")


"""
Завдання 4

Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.
"""


def sum_numbers(start_num, end_num):
    """

    :param start_num:
    :param end_num:
    :return:
    """
    if start_num > end_num:
        return 0
    if start_num <= end_num:
        return start_num + sum_numbers(start_num + 1, end_num)
    return None


startValueRange = int(input("Введите число с которого начинается последовательность: "))
endValueRange = int(input("Введите число с которым заканчивается последовательность: "))
print(f"Сума натуральных чисел от {startValueRange} до {endValueRange} ="
      f" {sum_numbers(startValueRange, endValueRange)}")

"""
Завдання 5

Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c.
Усередині цієї функції створити змінні x1, x2 зі значенням None
(спочатку приймаємо, що рівняння не має коренів) та функцію calc_rezult з
формальними параметрами зовнішньої функції quadratic_equation.
Всередині функції calc_rezult здійснити пошук дискримінанта,
згідно з результатом якого зробити розрахунок коренів рівняння.
Зовнішня функція quadratic_equation має повернути перелік значень коренів квадратного рівняння.
Надати можливість користувачеві ввести з клавіатури формальні
параметри для передачі їх у створену функцію quadratic_equation,
результати роботи функції відобразити на екрані.
"""
import math


def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    def calc_rezult(d):
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b + math.sqrt(d)) / (2 * a)
        elif d == 0:
            x1 = -b / (2 * a)
        else:
            x1 = None
            x2 = None

    d = pow(b, 2) - 4 * a * c
    calc_rezult(d)
    return x1, x2


a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
x1, x2 = quadratic_equation(a, b, c)
if x1 is None:
    print("Нет корней")
elif x1 == x2:
    print(f"Один корень = {x1}")
else:
    print(f"Первый корень = {x1}, второй конень = {x2}")
