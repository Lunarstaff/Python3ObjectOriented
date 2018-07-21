# MyFirstClass_v1.2.py
import math


# 定义Point类
class Point:
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


# 实例化两个点 P1，P2
point1 = Point()
point2 = Point()

# 重置P1
point1.reset()

# 移动P2到(5, 0)位置
point2.move(5, 0)

# 打印P2 到P1 的距离
print("P2 到 P1 的距离为：" + str(point2.calculate_distance(point1)))

# 断言：P2 到P1 的距离 恒等于 P1 到P2 的距离
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

# 移动P1 到(3, 4)位置
point1.move(3, 4)

# 打印P1 到P2 的距离
print("P1 到 P2 的距离为：" + str(point1.calculate_distance(point2)))

# 打印P2 到P1 的距离
print("P2 到 P1 的距离为：" + str(point2.calculate_distance(point1)))

# 打印P1 到P1 的距离
print("P1 到 P1 的距离为：" + str(point1.calculate_distance(point1)))
