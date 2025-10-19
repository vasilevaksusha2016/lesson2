from math import ceil


def square_area(side):
    return ceil(side * side)


side = float(input('Введите сторону квадрата: '))
print(f"Округленный вверх результат: {square_area(side)}")
