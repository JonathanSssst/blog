import numpy as np

# 创建示例数组
arr = np.arange(16).reshape(4, 4)
print("原始数组:\n", arr)

# 花式索引获取特定位置的元素
row_indices = [0, 2, 3]
col_indices = [1, 3, 0]
selected = arr[row_indices, col_indices]
print("花式索引结果:", selected)

# 使用ix_进行更复杂的索引
a = np.array([2, 3, 0])
b = np.array([0, 1, 3])
result = arr[np.ix_(a, b)]
print("使用ix_的复杂索引:\n", result)

# 布尔索引进行条件筛选
mask = (arr % 3 == 0) & (arr > 5)
filtered = arr[mask]
print("满足条件的元素:", filtered)