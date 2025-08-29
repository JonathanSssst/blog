import numpy as np

# 创建示例数组
arr = np.array([1, 4, 9, 16, 25])

# 数学函数
print("平方根:", np.sqrt(arr))
print("指数:", np.exp(arr))
print("对数:", np.log(arr))
print("三角函数:", np.sin(np.pi/6))

# 聚合函数
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print("数组总和:", np.sum(arr2d))
print("每列总和:", np.sum(arr2d, axis=0))
print("每行总和:", np.sum(arr2d, axis=1))
print("数组均值:", np.mean(arr2d))
print("数组标准差:", np.std(arr2d))
print("数组最大值:", np.max(arr2d))
print("数组最小值索引:", np.argmin(arr2d))