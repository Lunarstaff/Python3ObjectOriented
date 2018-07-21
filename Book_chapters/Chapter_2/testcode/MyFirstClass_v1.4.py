# MyFirstClass_v1.3.py
import math


# 定义Point类
class Point:
    '''
    Point类
    '''

    # 增加初始化函数
    def __init__(self, x=0, y=0):
        '''
        初始化方法：
            初始化一个新的Point类型对象的位置，如果没有给初始值，新的点类型对象默认位置为(0, 0)
        :param x:
        :param y:
        '''
        self.move(x, y)

    # 增加一个新的方法move，允许我们把点移动到任意位置
    def move(self, x, y):
        '''
        移动点对象到一个新的位置(x, y)
        :param x:
        :param y:
        :return:
        '''
        self.x = x
        self.y = y

    # def reset(self):
    #     self.x = 0
    #     self.y = 0

    # 重新定义reset方法
    def reset(self):
        '''
        重置点位置，把点位置设置为(0, 0)
        :return:
        '''
        self.move(0, 0)

    # 增加一个calculate_distance方法，接收另一个Point对象作为输入，然后返回这两个对象之间的距离
    def calculate_distance(self, other_point):
        '''
        计算两个点的直线距离，返回值为浮点数
        distance = sqrt((x1 - x2)**2 - (y1 - y2)**2)
        :param other_point:
        :return:
        '''
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
