import numpy as np

# 陷阱：整数除法
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
result = a / b  # 结果会是浮点数，即使输入是整数
print("除法结果类型:", result.dtype)

# 最佳实践：明确指定数据类型
a_float = a.astype(np.float64)
print("转换后类型:", a_float.dtype)

# 注意精度问题
large_int = np.array([2**60], dtype=np.int64)
print("大整数:", large_int)

# 转换为浮点数可能丢失精度
large_float = large_int.astype(np.float64)
print("转换后精度:", large_float)