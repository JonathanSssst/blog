# 导入整个模块
import math
print(math.pi)  # 输出: 3.141592653589793
print(math.sqrt(16))  # 输出: 4.0

# 导入模块中的特定函数
from math import pi, sqrt
print(pi)  # 输出: 3.141592653589793
print(sqrt(16))  # 输出: 4.0

# 导入模块并使用别名
import math as m
print(m.pi)  # 输出: 3.141592653589793
print(m.sqrt(16))  # 输出: 4.0

# 导入模块中的所有函数
from math import *
print(pi)  # 输出: 3.141592653589793
print(sqrt(16))  # 输出: 4.0