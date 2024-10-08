# Метод простых итераций
import numpy as np # импортируем библиотеку numpy, которая предоставляет функции и структуры
# данных для работы с массивами и матрицами


def iteration_method(x0, tol=1e-6, max_iter=100): # x0 - начальное приближение — массив из двух элементов
    # tol-допустимая ошибка для остановки итерационного процесса; max_iter-Максимальное количество итераций,
    # по умолчанию 100

    x = x0 # присваиваем переменной `x` начальное значение `x0`
    for _ in range(max_iter): # запускаем цикл, который будет продолжаться до тех пор, пока не достигнем
        # максимального количества итераций.

        # далле обновляем решение вычисляем новое приближение `x_new`
        x_new = np.array([np.sin(x[1] + 0.5) - 1, -np.cos(x[0] - 2)])
        if np.linalg.norm(x_new - x) < tol: # проверка сходимости, вычисляем норму разности между новым и
            # старым приближением. Если она меньше допустимого порога `tol`, мы считаем, что нашли решение,
            # и возвращаем `x_new`.

            return x_new
        x = x_new # обновляем значение, если сходимости не достигнуто, мы обновляем `x`, присваивая ему новое
        # значение `x_new`, и продолжаем итерацию.

    print("Достигнуто максимальное количество итераций.") # если за `max_iter` итерации сходимости не было
    # достигнуто, мы выводим сообщение об этом и возвращаем текущее значение `x`.

    return x

# далее устанавливаем начальное приближение `x0` равным `[1.0, 1.0]`, вызываем функцию `iteration_method`,
# и выводим найденное решение на экран.
x0 = np.array([1.0, 1.0])
solution_iter = iteration_method(x0)
print("Каушанский Андрей")
print("Решение методом простых итераций:", solution_iter)