import numpy as np

# 陷阱：不兼容的形状
a = np.array([[1, 2, 3]])      # 形状(1, 3)
b = np.array([[1], [2], [3]])  # 形状(3, 1)

# 这会成功，因为可以广播到(3, 3)
result = a + b
print("广播结果:\n", result)

# 但是这种情况会报错
try:
    c = np.array([1, 2, 3])      # 形状(3,)
    d = np.array([1, 2])         # 形状(2,)
    result = c + d
except ValueError as e:
    print("广播错误:", str(e))