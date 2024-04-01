import math
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

data = '0.866 -0.005 0.403 1.908 0.448 0.169 -0.731 -1.189 0.905 0.283 ' + \
       '2.431 1.409 0.191 -0.165 0.889 0.804 -2.131 -0.754 1.458 1.650 ' + \
       '0.110 1.757 -0.693 -0.732 1.073 -1.724 -1.810 0.947 -1.118 0.666 ' + \
       '0.026 0.885 0.011 -0.990 -0.104 0.174 -0.052 -0.182 1.813 0.346 ' + \
       '0.970 1.140 -1.105 0.894 1.547 -0.484 -0.086 -0.066 0.150 -0.264 ' + \
       ' 0.350 0.033 0.478 0.637 -0.033 -0.319 0.570 -0.837 -0.413 -1.640 ' + \
       '-0.795 -0.015 1.774 -1.568 0.302 -1.120 -0.917 -0.091 1.118 0.277 ' + \
       '-0.622 -0.554 -0.470 0.700 -0.656 1.460 1.701 0.630 -0.700 -0.674 ' + \
       ' 1.429 -1.163 -0.925 0.973 -0.052 0.409 -0.024 0.384 -0.350 0.203 ' + \
       '-2.084 0.100 0.001 -0.070 0.773 1.132 -0.769 -0.609 1.816 1.307 '
data = list(map(float, data.split()))

print("Исходные данные:")
print(data)
print()

print("Вариационный ряд: ")
print(sorted(data))
print()

print("Экстремальные значения:")
print(f"минимум: {min(data)}, максимум: {max(data)}, размах: {max(data) - min(data)}")
print()

diversity = [(i, data.count(i)) for i in set(data)]
n = len(diversity)
m = sum([i * j for i, j in diversity]) / n
d = sum([((i - m) ** 2) * j for i, j in diversity]) / n

print("Статистический ряд:")
for i, j in diversity:
    print(i, ":\t", j)
print()

print(f"Выборочное среднее: {m}")
print(f"Выборочная дисперсия: {d}")
print(f"Исправленная выборочная дисперсия: {n * d / (n - 1)}")
print(f"Среднеквадратическое отклонение: {sqrt(d)}")
print(f"Исправленное выборочное среднеквадратичное отклонение: {sqrt(n * d / (n - 1))}")
print()

# Эмпирическая функция распределения
# Интервальный ряд
def f(start, end):
    return sum([j for i, j in diversity if start <= i < end]) / n

print('Эмпирическая функция распределения:')
last_el = None
for i in sorted(data):
    print(f"{f(min(data), i)},\t{f'{last_el} <= ' if last_el else ''}x <= {i}")
    last_el = i
print()

x = np.linspace(min(data), max(data), 100)
y = [f(min(data), i) for i in x]
plt.plot(x, y, color='blue')
plt.title("Эмпирическая функция распределения")
plt.show()


# Полигон приведенных частот группированной выборки
h = (max(data) - min(data)) / (1 + math.log2(n))
x_start = min(data) - h / 2
x = np.arange(x_start, max(data), h)
y = [f(i, i + h) for i in x]

print("Интервальный ряд:")
print("Интервал\t\tЧастота\t\tЧастотность")
for i in range(len(x) - 1):
    print(f"({round(x[i], 2)},\t{round(x[i+1], 2)}):\t", end="")
    print(f"{sum([l for k, l in diversity if x[i] <= k < x[i + 1]])}\t\t\t", end="")
    print(f"{y[i]}")
print()

plt.plot(x, y)
plt.title("Полигон приведенных частот группированной выборки")
plt.show()


# Гистограмма приведенных частот группированной выборки
h = (max(data) - min(data)) / (1 + math.log2(n))
x_start = min(data) - h / 2
x = np.arange(x_start, max(data), h)
y = [f(i, i + h) for i in x]
plt.bar(x, y)
plt.title("Полигон приведенных частот группированной выборки")
plt.show()