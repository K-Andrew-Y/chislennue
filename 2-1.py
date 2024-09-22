import math

# Определяем функцию
def f(z):
    return 2 * z - 0.5 - math.sin(z + 0.5)

# Определяем первую производную функции
def f1(z):
    return 2 - math.cos(z + 0.5)

# Основная функция
def main():
    # Задаём интервал и точность вычислений
    a = 0
    b = 1
    eps = 0.0001
    n = 1

    print("Каушанский Андрей")
    print("Функция sin(x + 0.5) = 2*x - 0.5")
    print("Интервал X c [{:.3f};{:.3f}]".format(a, b))
    print("Точность вычислений {:.4f}".format(eps))
    print("Метод простых итераций")

    x = a
    lambda1 = 1 / f1(x)
    x_next = x - (lambda1) * f(x)
    c = abs(x - x_next)

    print("{:.5f} {:.5f} {:.5f} {}".format(x, x_next, c, n))

    while abs(x - x_next) >= eps and n < 2000:
        x = x_next
        lambda1 = 1 / f1(x)
        x_next = x - (lambda1) * f(x)
        n += 1
        c = abs(x - x_next)

        print("{:.5f} {:.5f} {:.5f} {}".format(x, x_next, c, n))

    print("{:.5f} {:.5f} {}".format(x, x_next, n))
    print("Корень уравнения {:.5f} найден с точностью {:.4f} за {} итерации".format(
        x_next, eps, n))

if __name__ == "__main__":
    main()