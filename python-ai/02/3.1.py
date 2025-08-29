# 创建列表
numbers = [1, 2, 3, 4, 5]
strings = ["Python", "AI", "Machine Learning"]
mixed = [1, "Python", 3.14, True]

# 访问列表元素
print(numbers[0])  # 输出: 1
print(strings[1])  # 输出: AI

# 修改列表元素
numbers[0] = 100
print(numbers)  # 输出: [100, 2, 3, 4, 5]

# 列表切片
print(numbers[1:3])  # 输出: [2, 3]
print(numbers[:3])   # 输出: [100, 2, 3]
print(numbers[3:])   # 输出: [4, 5]
print(numbers[-2:])  # 输出: [4, 5]

# 列表方法
numbers.append(6)      # 添加元素到列表末尾
print(numbers)         # 输出: [100, 2, 3, 4, 5, 6]

numbers.insert(1, 200) # 在指定位置插入元素
print(numbers)         # 输出: [100, 200, 2, 3, 4, 5, 6]

numbers.remove(3)      # 移除指定元素
print(numbers)         # 输出: [100, 200, 2, 4, 5, 6]

numbers.sort()         # 排序
print(numbers)         # 输出: [2, 4, 5, 6, 100, 200]