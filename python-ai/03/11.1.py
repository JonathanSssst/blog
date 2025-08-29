import numpy as np
import time

# 创建大数组
large_arr = np.arange(1000000)

# 低效方式：使用切片会创建副本
start = time.time()
subset_copy = large_arr[::2].copy() * 2  # 复制+计算
copy_time = time.time() - start

# 高效方式：使用视图
start = time.time()
subset_view = large_arr[::2] * 2  # 视图操作
view_time = time.time() - start

print(f"复制方式耗时: {copy_time:.4f}秒")
print(f"视图方式耗时: {view_time:.4f}秒")