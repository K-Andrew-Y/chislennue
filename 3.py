import math # импортируем математический модуль

# Задаём интервал и точность вычислений
a = 0
b = 1
eps = 0.0001 # допустимая погрешность для численных расчетов

def f(z):  # основная функция, для которой мы ищем корень
    return 2 * z - 0.5 - math.sin(z + 0.5) #

def f1(z):  # первая производная функции, которая используется в методе Ньютона
    return 2 - math.cos(z + 0.5)

def f2(z):  # вторая производная функции, которая также может помочь проанализировать поведение функции
    return math.sin(z + 0.5)

def metod_hord(xh, xk): # Эта функция реализует метод хорд, который используется для нахождения корня функции.
    # Метод использует линейную интерполяцию между двумя точками
    return xh - (f(xh) / (f(xk) - f(xh))) * (xk - xh)

def metod_Newton(xh, xk):# Эта функция реализует метод Ньютона для нахождения корня функции, используя
    # итерационную формулу
    return xk - (f(xk) / f1(xk))

def main():
    global xh, xk # определяем глобальные `xh` и `xk`, глобальньные чтобы их можно было менять
    xh, xk = 0, 0

   # даллее выводим информацию о программе
    print("Каушанский Андрей")
    print("Функция sin(x + 0,5) = 2*x - 0,5")
    print("Интервал X из [%.3f; %.3f]" % (a, b))
    print("Точность вычислений %.4f" % eps)

    # далее проверка условий
    print("f'(a)*f'(b) = %.3f" % (f1(a) * f1(b)))
    print("f''(a)*f''(b) = %.3f" % (f2(a) * f2(b)))

    if (f1(a) * f1(b) < 0) or (f2(a) * f2(b) < 0): # проверяются условия, если значение производных
        # на границах имеет разные знаки, тогда функция завершает выполнение.
        return

    # далее устанавливает значения `xh` и `xk`, исходя из значений функции и ее второй производной.
    # Это необходимо для начала итерационного процесса
    if f(a) * f2(a) > 0:
        xk = a
        xh = b
    elif f(b) * f2(b) > 0:
        xk = b
        xh = a

    # далее основной цикл. Повторяется, пока не будет достигнута допустимая погрешность (`eps`)
    # или не будет достигнут лимит итераций (100). Каждая итерация вычисляет следующее значение `xk` методом
    # Ньютона и значение `xh` методом хорд
    OK = -1
    n = 0

    print("Метод Ньютона\tМетод хорд")

    while (OK == -1) and (n < 100):
        xk = metod_Newton(xh, xk)
        xh = metod_hord(xh, xk)

        if abs(xk - xh) < eps: # если разница между `xk` и `xh` меньше `eps`, то `OK` = 1,
            # что означает, что условия завершения выполнены
            OK = 1

        n += 1

        print("%.5f\t\t\t%.5f" % (xk, xh)) # выводим текущие значения оба метода.


if __name__ == "__main__":
    main()