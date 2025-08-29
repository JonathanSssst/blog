import numpy as np

# 创建一维数组
arr = np.arange(12)
print("原始数组:", arr)

# 重塑为二维数组
reshaped = arr.reshape(3, 4)
print("重塑为3x4:\n", reshaped)

# 使用-1自动推断维度
reshaped2 = arr.reshape(2, -1)
print("自动推断列数:\n", reshaped2)

# 展平数组
flattened = reshaped.flatten()
print("展平后的数组:", flattened)

# 转置操作
transposed = reshaped.T
print("转置后的数组:\n", transposed)

# 添加新轴
arr = np.array([1, 2, 3])
row_vec = arr[np.newaxis, :]
col_vec = arr[:, np.newaxis]
print("行向量形状:", row_vec.shape)
print("列向量形状:", col_vec.shape)