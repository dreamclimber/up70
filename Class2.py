# 基类 Person
class Person_t:
    def __init__(self, name, age):
        self.name = name  # 姓名
        self.age = age    # 年龄

    def introduce(self):
        print(f"姓名：{self.name}, 年龄：{self.age}")


# 子类 Professor，继承自 Person
class Teacher_t(Person_t):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # 调用父类的构造方法
        self.subject = subject  # 教授科目

    def introduce(self):
        # 重写 introduce 方法
        print(f"姓名：{self.name}, 年龄：{self.age}, 教授科目：{self.subject}")


# 子类 Student，继承自 Person
class Student_t(Person_t):
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # 调用父类的构造方法
        self.grade = grade  # 年级

    def introduce(self):
        # 重写 introduce 方法
        print(f"姓名：{self.name}, 年龄：{self.age}, 年级：{self.grade}")


# 示例使用
professor = Teacher_t("Professor Li", 45, "物理学")
professor.introduce()  # 输出：姓名：李教授, 年龄：45, 教授科目：物理学

student = Student_t("Student Zhang", 18, "高一")
student.introduce()  # 输出：姓名：小张, 年龄：18, 年级：高一
