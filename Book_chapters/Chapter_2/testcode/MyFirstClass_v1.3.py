# MyFirstClass_v1.3.py
import math


# 定义Point类
class Point:
    # 增加初始化函数
    def __init__(self, x, y):
        self.move(x, y)

    # 增加一个新的方法move，允许我们把点移动到任意位置
    def move(self, x, y):
        self.x = x
        self.y = y

    # def reset(self):
    #     self.x = 0
    #     self.y = 0

    # 重新定义reset方法
    def reset(self):
        self.move(0, 0)

    # 增加一个calculate_distance方法，接收另一个Point对象作为输入，然后返回这两个对象之间的距离
    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


# 构造 一个P
point = Point(3, 5)
print(point.x, point.y)

# 输出为：
# 3 5
