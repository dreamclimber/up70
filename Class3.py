# 教师类 Teacher
class Teacher_t:
    def __init__(self, name, age, subject):
        self.name = name  # 教师姓名
        self.age = age    # 教师年龄
        self.subject = subject  # 教授科目

    # 输出Teacher信息
    def introduce(self):
        return f"姓名：{self.name}, 年龄：{self.age}, 教授科目：{self.subject}"


# 学生类 Student
class Student_t:
    def __init__(self, name, age, grade):
        self.name = name  # 学生姓名
        self.age = age    # 学生年龄
        self.grade = grade  # 学生年级

    # 输出Student信息
    def introduce(self):
        return f"姓名：{self.name}, 年龄：{self.age}, 年级：{self.grade}"


# 课程类 Course
class Course_t:
    def __init__(self, course_name, teacher):
        self.course_name = course_name  # 课程名称
        self.teacher = teacher  # 授课教师（Teacher 类实例）
        self.students = []  # 学生列表

    # 添加学生
    def addStudent(self, student):
        """添加学生到课程中"""
        if student not in self.students:
            self.students.append(student)
        else:
            print(f"{student.name} 已经选过此课程！")

    # 移除学生
    def removeStudent(self, student):
        """从课程中移除学生"""
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"{student.name} 未选此课程！")

    # 显示完整信息
    def showCourseInfo(self):
        """输出课程完整信息"""
        print(f"课程名称：{self.course_name}")
        print(f"授课教师：{self.teacher.introduce()}")
        print("选课学生：")
        if self.students:
            for student in self.students:
                print(student.introduce())
        else:
            print("暂无学生选课")


# 示例使用
# 创建教师和学生对象
teacher = Teacher_t("李教授", 45, "物理学")
student1 = Student_t("小张", 18, "高一")
student2 = Student_t("小李", 19, "高二")

# 创建课程对象
course = Course_t("物理学入门", teacher)

# 添加学生
course.addStudent(student1)
course.addStudent(student2)

# 展示课程信息
course.showCourseInfo()

# 移除学生
course.removeStudent(student1)

# 展示课程信息
course.showCourseInfo()
