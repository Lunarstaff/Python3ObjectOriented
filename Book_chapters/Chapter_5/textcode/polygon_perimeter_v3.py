import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


class Polygon:
    # v2
    # def __init__(self):
    #     self.vertices = []

    # v3,将Polygon类中的API变换一下，使它构造时能够接收多个点（一个Point对象的列表）作为参数
    def __init__(self, points=[]):
        self.vertices = []
        for point in points:
            # 如果传入的列表中某个元素不是Point类，就将其转换成Point类
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices + [self.vertices[0]]     # 将列表的第一个元素加到列表最后一个，形成闭合
        for i in range(len(self.vertices)):
            perimeter = perimeter + points[i].distance(points[i+1])
        return perimeter