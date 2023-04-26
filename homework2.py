# Завдання 1

# Напишіть програму, яка запитує у користувача два слова і виводить їх розділеними комою.

firstWord = input("Input first word: ")
secondWord = input("Input second word: ")
print(f'{firstWord}, {secondWord}\n')

# Завдання 2

# Напишіть програму, яка запитує три цілі числа a, b і x та друкує їх добуток.

firstNum = int(input("Input first number: "))
secondNum = int(input("Input second number: "))
thirdNum = int(input("Input third number: "))
print(firstNum * secondNum * thirdNum)

# Завдання 3
'''
Напишіть програму, яка розв'язує квадратне рівняння 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0 за формулами 𝑥1,2 =  −𝑏± b2−4ac−−−−−−−√
 / 2𝑎 . Значення a, b та c вводяться з клавіатури. Для знаходження кореня використовуйте оператор зведення в ступінь,
а не функцію math.sqrt, щоб отримати комплексні числа у випадку, якщо вираз під коренем негативний.
'''

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

discriminant = pow(b, 2) - 4 * a * c
if discriminant < 0:
    x1 = (-b + pow(discriminant, 1 / 2)) / (2 * a)
    x2 = (-b - pow(discriminant, 1 / 2)) / (2 * a)
    print(f'Первый корень: {x1} Второй корень: {x2}')
elif discriminant == 0:
    x = (-b + pow(discriminant, 1 / 2)) / (2 * a)
    print(f'"Корень один и равен =" {x}')
else:
    real_part = -b / (2 * a)
    imag_part = (-discriminant) ** 0.5 / (2 * a)
    print("Корни уровнения: ", complex(real_part, imag_part), "и", complex(real_part, -imag_part))

# Завдання 4

# Напишіть програму, в якій користувач вводить фразу з клавіатури, яка складається з 10 символів. На екрані виведіть суму ASCII-кодів символів введеного рядка.

phrase = input("Введите фразу с 10 символов: ")
x1 = ord(phrase[0])
x2 = ord(phrase[1])
x3 = ord(phrase[2])
x4 = ord(phrase[3])
x5 = ord(phrase[4])
x6 = ord(phrase[5])
x7 = ord(phrase[6])
x8 = ord(phrase[7])
x9 = ord(phrase[8])
x10 = ord(phrase[9])
print(x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10)

# Завдання 5

# Напишіть програму, яка вводить з клавіатури текст і виводить його в оберненому порядку.

text = input("Input your text: ")
print(text[::-1])

# Завдання 6

# Напишіть програму, яка запитує користувача радіус круга і виводить його площу. Формула площі круга: S= 𝜋𝑟 2 .

radius = int(input("Input circle radius: "))
print(f'Area of circle {3.14 * radius * 2}')

'''
Завдання 7

Напишіть програму, використовуючи знання про змінні типу цілих чисел,
щоб підрахувати, за який час транспортний засіб доїде з пункту А в пункт В,
якщо відомі такі дані: відстань від А до В = 700 км, швидкість автомобіля буде постійною та дорівнює 90 км/год.
Використовуйте формулу: Час = відстань / швидкість.
Створіть змінні length, куди запишіть відстань, velocity, куди запишіть швидкість та змінну driving_time, куди запишіть результат.
Після цього використайте метод print(), щоб вивести в консоль результат.
'''

length = 700
velocity = 90
driving_time = length / velocity
print(f'Час за який транспортний засіб доїде з пункту А в пункт В = {driving_time}')

'''
Завдання 8

Створіть змінну name, age, в якій зберігатиметься ім'я та вік користувача, введене з клавіатури.
Виведіть у консоль “My name is and I am ”, але зробіть рішення таким,
щоб використовувалася конкатенація рядків (через +) та приведення типу числа до рядка (str(...)).
Тобто, щоб якщо замінити змінні name і age, то в методі print() нічого не потрібно було би змінювати.
Наприклад, a = 15, print(“Value =” + str(a)) і буде “Value = 15”.
'''

name = input("Input your name: ")
age = input("Input your age: ")
print("My name is " + (name) + " and I am " + str(age) + " years old")
