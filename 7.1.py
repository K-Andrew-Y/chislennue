# Вычисление интеграла - метод трапеции
import math

def f(x):
    return (math.log(5 * x) ** 2)

def m_trapezia(a, b, n):
    h = (b - a) / n
    S = 0
    for i in range(n):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        S += 0.5 * (x2 - x1) * (f(x1) + f(x2))
    return S

def main():
    print("Каушанский Андрей")
    print("Вычисление интеграла методом трапеции")
    print("Подинтегральное выражение:")
    print("ln^2(5*x)")
    print("Нижний предел интегрирования: 1")
    print("Верхний предел интегрирования: 100")
    print("Значение интеграла число разбиений")

    for i in range(1, 1402, 100):
        y = m_trapezia(1, 100, i)
        print(f" {y:.4f} {i}")

if __name__ == '__main__':
    main()