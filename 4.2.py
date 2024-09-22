# Метод простых итераций
import numpy as np

def iteration_method(x0, tol=1e-6, max_iter=100):

    x = x0
    for _ in range(max_iter):

        x_new = np.array([np.sin(x[1] + 0.5) - 1, -np.cos(x[0] - 2)])
        if np.linalg.norm(x_new - x) < tol:

            return x_new
        x = x_new

    print("Достигнуто максимальное количество итераций.")
    return x

x0 = np.array([1.0, 1.0])
solution_iter = iteration_method(x0)
print("Каушанский Андрей")
print("Решение методом простых итераций:", solution_iter)