import numpy as np # импортируем библиотеку numpy, которая предоставляет функции и структуры
# данных для работы с массивами и матрицами

# Определим функции и якобиев матрицу
def f(x): # функция f(x), состоящий из двух элементов (например, `x[0]` и `x[1]`), и
    # возвращает массив из двух значений. Эти значения представляют систему уравнений, которую мы хотим решить:

    return np.array([
        np.sin(x[1] + 0.5) - x[0] - 1,
        np.cos(x[0] - 2) + x[1]
    ])

def jacobian(x): # функция `jacobian` вычисляет матрицу Якоби для системы уравнений.
    return np.array([
        [-1, np.cos(x[1] + 0.5)],
        [np.sin(x[0] - 2), 1]
    ])

# далее функция `newton_method` реализует сам метод Ньютона
def newton_method(x0, tol=1e-6, max_iter=100): # x0 — начальное приближение; tol — допустимая ошибка
    # (по умолчанию \(1 \times 10^{-6}\)); max_iter — максимальное количество итераций (по умолчанию 100).
    x = x0 # инициализируем x равным x0
    for _ in range(max_iter): # Вычисляем значения функции `f` в текущей точке `x` (`fx`) и значение Якобиана `J`
        fx = f(x)
        J = jacobian(x)
        try:
            delta_x = np.linalg.solve(J, -fx) # решаем линейную систему уравнений для нахождения
            # изменения `delta_x` с использованием linalg.solve()

        except np.linalg.LinAlgError: # если не удается решить обрабатываем исключение и завершаем работу функции.
            print("Ошибка при решении системы уравнений.")
            return None
        x = x + delta_x # обновляем `x`, добавляя `delta_x`.
        if np.linalg.norm(delta_x) < tol: # проверяем условие остановки: если норма вектора `delta_x`
            # становится меньше допускаемой ошибки `tol`, возвращаем найденное значение `x`.

            return x
    print("Каушанский Андрей")
    print("Достигнуто максимальное количество итераций.") # если достигается максимальное количество итераций,
    # выводим сообщение.

    return x

# Начальное приближение
x0 = np.array([1.0, 1.0]) # здесь задается начальное приближение `x0 = [1.0, 1.0]`,
# после чего запускается метод Ньютона и решение выводится на экран.
# array - определяет тип объекта

solution_newton = newton_method(x0)
print("Решение методом Ньютона:", solution_newton)