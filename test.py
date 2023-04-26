def quadratic_equation(a, b, c):
    """Функція для розв'язання квадратного рівняння"""
    x1 = None
    x2 = None

    def calc_rezult(d):
        """Функція для розрахунку коренів квадратного рівняння"""
        if d > 0:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
        elif d == 0:
            x1 = -b / (2 * a)
        else:
            x1 = None
            x2 = None

    # Розрахунок дискримінанта
    discriminant = b ** 2 - 4 * a * c
    calc_rezult(discriminant)

    # Повернення значень коренів
    return x1, x2


# Введення коефіцієнтів квадратного рівняння користувачем
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Виклик функції quadratic_equation для розв'язання квадратного рівняння
x1, x2 = quadratic_equation(a, b, c)

# Виведення результатів
if x1 is None:
    print("Рівняння не має реальних коренів")
elif x1 == x2:
    print(f"Рівняння має один корінь: x = {x1}")
else:
    print(f"Рівняння має два корені: x1 = {x1}, x2 = {x2}")
