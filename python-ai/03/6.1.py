import numpy as np

# 示例1：标量与数组的广播
arr = np.array([1, 2, 3, 4])
result = arr + 10  # 标量10被广播到数组的每个元素
print("标量广播:", result)

# 示例2：一维数组与二维数组的广播
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
arr1d = np.array([10, 20, 30])
result = arr2d + arr1d  # 一维数组被广播到二维数组的每一行
print("一维到二维广播:\n", result)

# 示例3：更复杂的广播
a = np.array([[1], [2], [3]])  # 形状(3, 1)
b = np.array([10, 20, 30])      # 形状(3,)
result = a + b                  # 广播为(3, 3)
print("复杂广播:\n", result)