import numpy as np

def main():
    n = 100
    # Создаем массивы для коэффициентов
    A = np.zeros(n + 1)
    B = np.zeros(n + 1)
    C = np.zeros(n + 1)
    D = np.zeros(n + 1)

    print("Каушанский Андрей. Метод прогонки")

    # Начальные значения
    A[1] = 0
    B[1] = 2
    C[1] = 1
    D[1] = 10 * 6  # мой вариант 6, поэтому по формуле d = 10*k = 60

    for i in range(2, n):
        A[i] = 1
        C[i] = 1
        B[i] = 2
        D[i] = 60

    # Значения для последнего числа в ряду
    A[n] = 1
    B[n] = 2
    C[n] = 0
    D[n] = 60

    # Выводим коэффициенты
    print("A =", A[1:n + 1])
    print("C =", C[1:n + 1])
    print("B =", B[1:n])  # До n-1
    print("D =", D[1:n + 1])

    # ---------- Прямой ход --------------------------

    X = np.zeros(n + 1)
    U = np.zeros(n + 1)
    V = np.zeros(n + 1)

    U[1] = -(C[1] / B[1])
    V[1] = D[1] / B[1]

    for i in range(2, n):
        U[i] = -C[i] / (B[i] + A[i] * U[i - 1])
        V[i] = (D[i] - A[i] * V[i - 1]) / (B[i] + A[i] * U[i - 1])

    # ---------- Обратный ход -----------------------

    X[n] = (D[n] - A[n] * V[n - 1]) / (B[n] + A[n] * U[n - 1])
    for i in range(n - 1, 0, -1):
        X[i] = U[i] * X[i + 1] + V[i]

    # Выводим решения
    print("\nЗначения X")
    for i in range(1, n + 1):
        print(f"{X[i]:.4f}")

if __name__ == "__main__":
    main()