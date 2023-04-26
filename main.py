"""
Завдання 2

Відкрийте файл fix_me.py із папки homework.
Використовуючи звичайний текстовий редактор (Notepad),
виправте всі помилки оформлення коду згідно з PEP 8.
"""

from math import pi
from math import e

MY_PRINT = 5
coUnt = int(input('Введите количество повторов: '))
print(MY_PRINT * coUnt)
print(pi * MY_PRINT * coUnt)
print(e * 2)
while MY_PRINT >= 0:
    MY_PRINT -= 1
MY_STR = 'my string'
MY_SUM = 0
for elem in MY_STR:
    MY_SUM += pow(MY_STR.find(elem), 2)
    print("sum =", MY_SUM)


def my_func(atr=1):
    """

    :param atr:
    :return:
    """
    print('atr', atr)


print(my_func(atr=5))
