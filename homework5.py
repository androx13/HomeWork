# Завдання 1
#
# Створіть програму, яка зчитує рядок, в якому знаходиться ПІБ користувача і перевіряє,
# чи складається рядок з літер, при чому кожне слово має бути записане з великої літери.
# Вивести результат на екран.

name = input("Введите ФИО пользователя: ")
if name.istitle() and name.replace(" ", "").isalpha():
    print("Строка состоит из букв и каждое слово начинается с заглавной")
else:
    print("Строка не состоит из букв или каждое слово не начинается с заглавной")

# Завдання 2
#
# Напишіть програму, в якій користувач вводить із клавіатури діапазон чисел
# (в діапазоні має бути не менше 5 чисел).
# Вивести на екран суму другого, передостаннього, а також середнього арифметичного значення даної послідовності.

nums = input("Введите диапозон чисел, через пробел(не меньше 5): ")
nums_tuple = nums.split()
while len(nums_tuple) < 5:
    nums = input("Введите диапозон чисел, через пробел(не меньше 5): ")
    nums_tuple = nums.split()
nums_tuple = tuple(map(int, nums_tuple))
print("Сумма второго и предпоследнего элемента равна =", nums_tuple[1] + nums_tuple[-2])
print("Среднее арифметическое значение этой последовательности равно = ", sum(nums_tuple) / len(nums_tuple))

# Завдання 3
#
# Напишіть програму, яка на вхід отримує параметри кольору (в діапазоні від 0 до 255 для кожного кольору)
# у форматі RGB і виводить на екран кортеж, у якому зберігається колір.

r = int(input("Введите параметр цвета R = "))
while not 0 <= r <= 255:
    r = int(input("Ошибка \nВведите параметр цвета R = "))
g = int(input("Введите параметр цвета G = "))
while not 0 <= g <= 255:
    g = int(input("Ошибка \nВведите параметр цвета G = "))
b = int(input("Введите параметр цвета B = "))
while not 0 <= b <= 255:
    b = int(input("Ошибка \nВведите параметр цвета B = "))

rgb = (r, g, b)
print("Цвет в RGB =", rgb)

# Завдання 4
#
# Ознайомтеся за допомогою документації з класами namedtuple та deque модуля collections.
# Створіть фабрику іменованих кортежів оцінок для учнів однієї групи з предметів:
# алгебра, геометрія, історія, інформатика, географія. Вивести дані на екран.

import random
from collections import namedtuple, deque

mark = namedtuple("Marks", ["algebra", "geometry", "history", "informatics", "geography"])
student_marks = deque([
    mark(int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100),
         int(random.random() * 100)),
    mark(int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100),
         int(random.random() * 100)),
    mark(int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100),
         int(random.random() * 100)),
    mark(int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100),
         int(random.random() * 100)),
    mark(int(random.random() * 100), int(random.random() * 100), int(random.random() * 100), int(random.random() * 100),
         int(random.random() * 100))
])
for value, marks in enumerate(student_marks, 1):
    print(f"Ученик {value}: алгебра - {marks.algebra}, геометрия - {marks.geometry}, история - {marks.history}, "
          f"информатика - {marks.informatics}, география - {marks.geography}")

# Завдання 5
#
# Напишіть програму, яка вводить з клавіатури послідовність чисел,
# перетворює послідовність на кортеж і виводить його відсортованим у порядку зростання.

nums = input("Введите последовательность чисел: ")
nums_tuple = tuple(nums.split())
nums_tuple = tuple(map(int, nums_tuple))
print(sorted(nums_tuple))

# Завдання 6
#
# Напишіть програму для аналізу фідбеку від відвідувачів курорту «Морська зірка»,
# яка повинна знаходити згадки про меню, спортзал,
# обслуговування(за кожне знайдене співпадіння нараховується 5% знижки на наступне відвідування).
# Якщо фідбек перевищив 60 символів, відвідувачу надається додаткова знижка 15% на наступне відвідування.

feedback = input("Введите ваш отзыв: ")
feedback = feedback.lower()
discount = 0
my_tuple = ("меню", "спортзал", "обслуживание")
for n in my_tuple:
    if n in feedback:
        discount += 5
if len(feedback) > 60:
    discount += 15
print("Ваша скидка на следующие посещение равна - ", discount)
