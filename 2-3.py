import math

# Задаём интервал и точность вычислений
def f(z):  # Функция
    return 2 * z - 0.5 - math.sin(z + 0.5)

def main():
    a = 0
    b = 1
    eps = 0.0001
    n = 0

    print("Каушанский Андрей")
    print("Функция sin(x + 0,5) = 2*x - 0,5")
    print("Интервал X из [%.3f; %.3f]" % (a, b))
    print("Точность вычислений %.4f" % eps)
    print("Метод половинного деления")

    while abs(a - b) >= eps:
        c = (a + b) / 2
        print(c)

        if f(c) * f(a) <= 0:
            b = c
            print(b)
        else:
            a = c
            print(a)

        n += 1

    print("Число шагов = %d" % n)

if __name__ == "__main__":
    main()