# Вычисление интеграла методом прямоугольников
import math

def f(x):
    return (math.log(5 * x) ** 2)

def m_pryamo(a, b, n):
    h = (b - a) / n
    S = 0
    for i in range(n - 1):
        x = a + i * h
        S += f(x)
    S *= h
    return S

def main():
    print("Каушанский Андрей")
    print("Вычисление интеграла методом прямоугольников")
    print("Подинтегральное выражение:")
    print("ln^2(5*x)")
    print("Нижний предел интегрирования: 1")
    print("Верхний предел интегрирования: 100")
    print("Значение интеграла число разбиений")

    for i in range(100, 20001, 1000):
        y = m_pryamo(1, 100, i)
        print(f"   {y:.4f}         {i}")

if __name__ == "__main__":
    main()