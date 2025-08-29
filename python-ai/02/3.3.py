# 创建字典
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "AI", "Data Science"]
}

# 访问字典元素
print(person["name"])  # 输出: Alice
print(person.get("age"))  # 输出: 30

# 修改字典元素
person["age"] = 31
print(person)  # 输出: {'name': 'Alice', 'age': 31, 'city': 'New York', 'skills': ['Python', 'AI', 'Data Science']}

# 添加新的键值对
person["email"] = "alice@example.com"
print(person)  # 输出: {'name': 'Alice', 'age': 31, 'city': 'New York', 'skills': ['Python', 'AI', 'Data Science'], 'email': 'alice@example.com'}

# 遍历字典
for key, value in person.items():
    print(f"{key}: {value}")