"""
Завдання 3

Створіть інженерний калькулятор з використанням модуля math,
в якому передбачене меню. Під час створення дотримуйтесь правил специфікації PEP 8.
"""
import math
num1 = 0
num2 = 0


def root(var_one):
    """
    Найти корень.
    :param var_one:
    :return:
    """
    if var_one >= 0:
        return math.sqrt(var_one)
    return "Ошибка, у отрицательного числа нет корней"


def square(var_one):
    """
    Возвести число в квадрат
    :param var_one:
    :return:
    """
    return pow(var_one, 2)


def power(var_one, var_two):
    """
    Возвести число в степень
    :param var_one:
    :param var_two:
    :return:
    """
    return pow(var_one, var_two)


def sin(var_one):
    """
    Синус числа
    :param var_one:
    :return:
    """
    return math.sin(var_one)


def cos(var_one):
    """
    Косинус числа
    :param var_one:
    :return:
    """
    return math.cos(var_one)


def tang(var_one):
    """
    Тангенс числа
    :param var_one:
    :return:
    """
    return math.tan(var_one)


def cotang(var_one):
    """
    Котангенс числа
    :param var_one:
    :return:
    """
    return 1 / math.tan(var_one)


def log(var_one, var_two):
    """
    Логорифм по основанию
    :param var_one:
    :param var_two:
    :return:
    """
    return math.log(var_one, var_two)


def arcsin(var_one):
    """
    Арксинус
    :param var_one:
    :return:
    """
    return math.asin(var_one)


def arccos(var_one):
    """
    Арккосинус
    :param var_one:
    :return:
    """
    return math.acos(var_one)


def arctang(var_one):
    """
    Арктангенс
    :param var_one:
    :return:
    """
    return math.atan(var_one)


def arccotang(var_one):
    """
    Арккотангенс
    :param var_one:
    :return:
    """
    return math.pi / 2 - math.atan(var_one)


while True:
    option = input("Меню:\n"
                   "----------\n"
                   "1. Найти корень\n"
                   "2. Возвести число в квадрат\n"
                   "3. Возвести число в степень\n"
                   "4. Синус числа\n"
                   "5. Косинус числа\n"
                   "6. Тангенс числа\n"
                   "7. Котангенс числа\n"
                   "8. Логорифм по основанию\n"
                   "9. Арксинус числа\n"
                   "10. Арккосинус\n"
                   "11. Арктангенс\n"
                   "12. Арккотангенс\n"
                   "13. Выход\n"
                   "----------\n"
                   "Выберите операцию: ")
    if option in ["1", "2", "3", "4", "5", "6", "7"]:
        num1 = float(input("Введите первое число: "))
        if option in ("3", "8"):
            num2 = float(input("Введите второе число: "))
            print()

    match option:
        case "1":
            print("Результат: ", root(num1), "\n")
        case "2":
            print("Результат: ", square(num1), "\n")
        case "3":
            print("Результат: ", power(num1, num2), "\n")
        case "4":
            print("Результат: ", sin(num1), "\n")
        case "5":
            print("Результат: ", cos(num1), "\n")
        case "6":
            print("Результат: ", tang(num1), "\n")
        case "7":
            print("Результат: ", cotang(num1), "\n")
        case "8":
            print("Результат: ", log(num1, num2), "\n")
        case "9":
            print("Результат: ", arcsin(num1), "\n")
        case "10":
            print("Результат: ", arccos(num1), "\n")
        case "11":
            print("Результат: ", arctang(num1), "\n")
        case "12":
            print("Результат: ", arccotang(num1), "\n")
        case "13":
            break
        case _:
            print("Неверный ввод, попробуйте еще раз\n")


"""
Завдання 4

Створіть магазин канцтоварів використовуючи списки для зберігання елементів.
Для додавання елементів створіть функцію, яка буде запитувати дані в користувача
і зібрані дані у вигляді кортежу додавати у створений список на початку.
Результат вивести на екран. Під час створення дотримуйтесь правил специфікації PEP 8.
"""
items_l = []


def add_item(item):
    """
    Добовляем товар в список
    :param item:
    :return:
    """
    name = input("Введите наименование товара: ")
    price = float(input("Введите цену: "))
    quantity = int(input("Введите количество: "))
    print("Товар добавлен успешно\n")
    item = (name, price, quantity)
    items_l.insert(0, item)


def show_items(item_list):
    """
    Выводим список на экран
    :param item_list:
    :return:
    """
    print("Название товара | Цена | Количество")
    for item in items_l:
        print(f"{item[0]} | {item[1]} | {item[2]}")


while True:
    option = input("Меню\n"
                   "------------------------------------\n"
                   "1. Добавить товар.\n"
                   "2. Посмотреть список товаров\n"
                   "3. Выход\n"
                   "------------------------------------\n"
                   "Выберите опцию: ")
    match option:
        case "1":
            add_item(items_l)
        case "2":
            show_items(items_l)
        case "3":
            break
        case _:
            print("Неверный ввод, попробуйте еще раз\n")
