# 定义函数
def add(a, b):
    """计算两个数的和"""
    return a + b

# 调用函数
result = add(3, 5)
print(result)  # 输出: 8

# 带有默认参数的函数
def greet(name, greeting="Hello"):
    """问候某人"""
    return f"{greeting}, {name}!"

print(greet("Alice"))       # 输出: Hello, Alice!
print(greet("Bob", "Hi"))  # 输出: Hi, Bob!

# 可变参数函数
def sum_numbers(*args):
    """计算任意数量数字的和"""
    total = 0
    for num in args:
        total += num
    return total

print(sum_numbers(1, 2, 3))        # 输出: 6
print(sum_numbers(1, 2, 3, 4, 5))  # 输出: 15