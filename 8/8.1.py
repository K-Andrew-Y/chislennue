import math

def f(x):
    return (math.log(5 * x) ** 2)

def simpson_integral(a, b, eps):
    print("Каушанский Андрей")
    print("Вычисление интеграла методом Симпсона")
    print("Подинтегральное выражение:")
    print("ln^2(5*x)")
    print("Нижний предел интегрирования:", a)
    print("Верхний предел интегрирования:", b)
    print("Значение интеграла число разбиений")

    I = eps + 1
    I1 = 0  # I1 - новое, с большим N.

    N = 2
    while (N <= 4) or (abs(I1 - I) > eps):
        h = (b - a) / (2 * N)  # Шаг интегрирования.
        sum2 = 0  # Для чётных индексов
        sum4 = 0  # Для нечётных индексов

        for i in range(1, 2 * N, 2):
            sum4 += f(a + h * i)  # Значения с нечётными индексами, которые нужно умножить на 4.
            sum2 += f(a + h * (i + 1))  # Значения с чётными индексами, которые нужно умножить на 2.

        sum = f(a) + 4 * sum4 + 2 * sum2 - f(b)  # Отнимаем значение f(b), так как ранее прибавили его дважды.
        I = I1
        I1 = (h / 3) * sum

        print(f"{I1:10.5f} {N}")
        N *= 2  # Увеличиваем число разбиений

    return I1

# Параметры интегрирования
a = 1.0
b = 100.0
eps = 0.0001

# Вызов функции для вычисления интеграла
simpson_integral(a, b, eps)