import numpy as np
import time

# 创建测试数组
arr = np.random.randn(10000)

# 低效方式：使用Python循环
start = time.time()
sum_manual = 0
for x in arr:
    sum_manual += x
manual_time = time.time() - start

# 高效方式：使用NumPy内置函数
start = time.time()
sum_numpy = np.sum(arr)
numpy_time = time.time() - start

print(f"手动求和耗时: {manual_time:.4f}秒")
print(f"NumPy求和耗时: {numpy_time:.4f}秒")