# Метод Ньютона\tМетод хорд
import math

# Задаём интервал и точность вычислений
a = 0
b = 1
eps = 0.0001

def f(z):  # Функция
    return 2 * z - 0.5 - math.sin(z + 0.5)

def f1(z):  # 1-я производная
    return 2 - math.cos(z + 0.5)

def f2(z):  # 2-я производная
    return math.sin(z + 0.5)

def metod_hord(xh, xk):
    return xh - (f(xh) / (f(xk) - f(xh))) * (xk - xh)

def metod_Newton(xh, xk):
    return xk - (f(xk) / f1(xk))

def main():
    global xh, xk
    xh, xk = 0, 0

    print("Каушанский Андрей")
    print("Функция sin(x + 0,5) = 2*x - 0,5")
    print("Интервал X из [%.3f; %.3f]" % (a, b))
    print("Точность вычислений %.4f" % eps)

    print("f'(a)*f'(b) = %.3f" % (f1(a) * f1(b)))
    print("f''(a)*f''(b) = %.3f" % (f2(a) * f2(b)))

    if (f1(a) * f1(b) < 0) or (f2(a) * f2(b) < 0):
        return

    if f(a) * f2(a) > 0:
        xk = a
        xh = b
    elif f(b) * f2(b) > 0:
        xk = b
        xh = a

    OK = -1
    n = 0

    print("Метод Ньютона\tМетод хорд")

    while (OK == -1) and (n < 100):
        xk = metod_Newton(xh, xk)
        xh = metod_hord(xh, xk)

        if abs(xk - xh) < eps:
            OK = 1

        n += 1

        print("%.5f\t\t\t%.5f" % (xk, xh))

if __name__ == "__main__":
    main()