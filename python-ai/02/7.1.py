# 定义类
class Person:
    """人员类"""
    # 类变量
    species = "Homo sapiens"
        
        # 初始化方法
    def __init__(self, name, age):
            # 实例变量
            self.name = name
            self.age = age
        
        # 实例方法
    def greet(self):
            return f"Hello, my name is {self.name}."
        
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday! Now I'm {self.age} years old."
        
    # 类方法
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2023
        age = current_year - birth_year
        return cls(name, age)
    
    # 静态方法
    @staticmethod
    def is_adult(age):
        return age >= 18

# 创建对象
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 访问类变量
print(Person.species)  # 输出: Homo sapiens

# 访问实例变量
print(person1.name)  # 输出: Alice
print(person2.age)  # 输出: 25

# 调用实例方法
print(person1.greet())  # 输出: Hello, my name is Alice.
print(person2.celebrate_birthday())  # 输出: Happy Birthday! Now I'm 26 years old.

# 调用类方法
person3 = Person.from_birth_year("Charlie", 1990)
print(person3.name, person3.age)  # 输出: Charlie 33

# 调用静态方法
print(Person.is_adult(20))  # 输出: True
print(Person.is_adult(15))  # 输出: False

# 继承
class Student(Person):
    """学生类，继承自Person类"""
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def study(self, subject):
        return f"{self.name} is studying {subject}."

# 创建子类对象
student = Student("David", 20, "12345")
print(student.greet())  # 输出: Hello, my name is David.
print(student.study("AI"))  # 输出: David is studying AI.

# 多态
def celebrate(person):
    return person.celebrate_birthday()

print(celebrate(person1))  # 输出: Happy Birthday! Now I'm 31 years old.
print(celebrate(student))  # 输出: Happy Birthday! Now I'm 21 years old.