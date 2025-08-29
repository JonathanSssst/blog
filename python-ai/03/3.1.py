import numpy as np

# 1. 从列表创建数组
arr1 = np.array([1, 2, 3, 4, 5])
print("从列表创建:", arr1)

# 2. 创建全0数组
zeros = np.zeros((3, 4))  # 3行4列的二维数组
print("全0数组:\n", zeros)

# 3. 创建全1数组
ones = np.ones((2, 3, 4))  # 三维数组
print("全1数组形状:", ones.shape)

# 4. 创建单位矩阵
eye = np.eye(4)  # 4x4单位矩阵
print("单位矩阵:\n", eye)

# 5. 创建随机数组
random_arr = np.random.rand(3, 3)  # 0-1之间的随机数
print("随机数组:\n", random_arr)

# 6. 创建等差数列
arange_arr = np.arange(0, 10, 2)  # 从0到10，步长为2
print("等差数列:", arange_arr)

# 7. 创建等间隔数
linspace_arr = np.linspace(0, 1, 5)  # 0到1之间等间隔的5个数
print("等间隔数:", linspace_arr)