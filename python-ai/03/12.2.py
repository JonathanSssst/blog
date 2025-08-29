import numpy as np

# 陷阱：意外的修改
original = np.array([1, 2, 3, 4])
slice_view = original[1:3]  # 这是一个视图，不是副本
slice_view[0] = 999
print("原始数组被修改:", original)  # [1 999 3 4]

# 最佳实践：明确创建副本
original = np.array([1, 2, 3, 4])
slice_copy = original[1:3].copy()
slice_copy[0] = 999
print("原始数组保持不变:", original)  # [1 2 3 4]