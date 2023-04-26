import random
from collections import namedtuple, deque

# Створення іменованого кортежу оцінок
Mark = namedtuple('Mark', ['algebra', 'geometry', 'history', 'informatics', 'geography'])

# Фабрика оцінок для учнів групи
score = int(random.random() * 100)
student_marks = deque([
    Mark(score, score, score, score, score),
    Mark(score, score, score, score, score),
    Mark(5, 5, 4, 3, 4),
    Mark(4, 3, 5, 4, 3),
    Mark(5, 4, 4, 5, 4)
])

# Виведення на екран
for i, marks in enumerate(student_marks, 1):
    print(f"Учень {i}: алгебра - {marks.algebra}, геометрія - {marks.geometry}, історія - {marks.history}, "
          f"інформатика - {marks.informatics}, географія - {marks.geography}")
