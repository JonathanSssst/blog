import numpy as np

# 创建两个数组
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# 向量化加法
result = a + b
print("向量化加法:", result)

# 向量化乘法
result = a * b
print("向量化乘法:", result)

# 数学函数
result = np.sqrt(a)
print("平方根:", result)

# 与Python循环的性能对比
import time

# 使用NumPy向量化
start = time.time()
large_arr = np.arange(1000000)
squared_np = large_arr ** 2
np_time = time.time() - start

# 使用Python循环
start = time.time()
large_list = list(range(1000000))
squared_py = [x**2 for x in large_list]
py_time = time.time() - start

print(f"NumPy向量化耗时: {np_time:.4f}秒")
print(f"Python循环耗时: {py_time:.4f}秒")