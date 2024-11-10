class Person_t:
    def __init__(self, name, age):
        self.name = name  # 姓名
        self.age = age    # 年龄

    def introduce(self):
        print(f"姓名：{self.name}, 年龄：{self.age}")

# 示例使用
person = Person_t("Lisunyong", 25)
person.introduce()
