import numpy as np

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
print(sorted(data))
num_count = len(data)
k = np.sqrt(num_count)
a = -2.15
b = 2.45
h = round((b - a) / k, 1)
print(f"{num_count=}")
print(f"{k=}")
print(f"{a=}")
print(f"{b=}")
print(f"{h=}")


#Интервалы
nums = []
borders = []
x_i_star = []
n_i = []
p_i_star = []

intervals_count = round((b - a) / h)
nums = list(range(intervals_count))
borders = [(a + h * i, a + h * (i + 1)) for i in range(intervals_count - 1)]
borders.append((a + (intervals_count - 1) * h, b))
x_i_star = [(a + b) / 2 for a, b in borders]
n_i = [
       len([num for num in data if round(a + i * h,3) <= num < round(a + h * (i + 1),3)])
       for i in range(intervals_count)
]

# print([a + i * h
#        for i in range(intervals_count)
# ])
print(sum(n_i))

print(f"Номера интервалов: ", nums)
print(f"Границы интервалов: ", borders)
print(f"x_i_*: ", x_i_star)
print(f"n_i: ", n_i)
print(f"p_i: ", p_i_star)




