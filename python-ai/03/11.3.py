import numpy as np

# 创建二维数组
arr = np.arange(1000000).reshape(1000, 1000)

# 检查内存布局
print("C连续:", arr.flags['C_CONTIGUOUS'])
print("F连续:", arr.flags['F_CONTIGUOUS'])

# 转置后的内存布局
transposed = arr.T
print("转置后C连续:", transposed.flags['C_CONTIGUOUS'])

# 优化内存访问
optimized = np.ascontiguousarray(transposed)
print("优化后C连续:", optimized.flags['C_CONTIGUOUS'])