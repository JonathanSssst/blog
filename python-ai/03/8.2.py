import numpy as np

# 创建矩阵
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 矩阵乘法
result = np.dot(A, B)
print("矩阵乘法:\n", result)

# 或者使用@运算符（Python 3.5+）
result = A @ B
print("使用@运算符:\n", result)

# 矩阵转置
transpose = A.T
print("矩阵转置:\n", transpose)

# 计算行列式
det = np.linalg.det(A)
print("行列式:", det)

# 计算逆矩阵
inverse = np.linalg.inv(A)
print("逆矩阵:\n", inverse)

# 计算特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)
print("特征值:", eigenvalues)
print("特征向量:\n", eigenvectors)

# 解线性方程组 Ax = b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print("方程组的解:", x)