# методом Ньютона
import numpy as np

# Определим функции и якобиев матрицу
def f(x):
    return np.array([
        np.sin(x[1] + 0.5) - x[0] - 1,
        np.cos(x[0] - 2) + x[1]
    ])

def jacobian(x):
    return np.array([
        [-1, np.cos(x[1] + 0.5)],
        [np.sin(x[0] - 2), 1]
    ])

def newton_method(x0, tol=1e-6, max_iter=100):

    x = x0
    for _ in range(max_iter):
        fx = f(x)
        J = jacobian(x)
        try:
            delta_x = np.linalg.solve(J, -fx)

        except np.linalg.LinAlgError:
            print("Ошибка при решении системы уравнений.")
            return None
        x = x + delta_x
        if np.linalg.norm(delta_x) < tol:

            return x
    print("Каушанский Андрей")
    print("Достигнуто максимальное количество итераций.")

    return x

# Начальное приближение
x0 = np.array([1.0, 1.0])

solution_newton = newton_method(x0)
print("Решение методом Ньютона:", solution_newton)