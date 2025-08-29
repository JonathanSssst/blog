# 创建元组
t = (1, 2, 3, "Python")

# 访问元组元素
print(t[0])  # 输出: 1
print(t[-1]) # 输出: Python

# 元组切片
print(t[1:3])  # 输出: (2, 3)

# 尝试修改元组（会报错）
# t[0] = 100  # TypeError: 'tuple' object does not support item assignment