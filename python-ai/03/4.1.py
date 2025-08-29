import numpy as np

# 创建一个示例数组
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("数组形状:", arr.shape)        # (3, 4)
print("数组维度:", arr.ndim)         # 2
print("数组大小:", arr.size)         # 12
print("数据类型:", arr.dtype)        # int64
print("数组内存大小:", arr.nbytes, "字节")

# 基本索引
print("第一行:", arr[0])
print("第二列:", arr[:, 1])
print("子数组:", arr[1:3, 0:3])

# 布尔索引
mask = arr > 5
print("大于5的元素:", arr[mask])

# 花式索引
indices = [0, 2]
print("指定行:", arr[indices])