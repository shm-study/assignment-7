
class Triangle():
    base = 0
    height = 0

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

    def __str__(self):
        return "밑변은 " + str(self.base) + "이고 " + "높이는 " + str(self.height) + "인 삼각형입니다."


a = Triangle(3, 4)

print(a.area())  # 6
print(a)  # 밑변은 3 이고 높이는 4 인 삼각형 입니다.




