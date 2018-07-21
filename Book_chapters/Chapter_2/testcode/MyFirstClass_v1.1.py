# MyFirstClass_v1.1.py


# 定义Point类，增加reset方法
class Point:
    def reset(self):
        self.x = 0
        self.y = 0


# 实例化
p = Point()
# 赋值
p.x = 5
p.y = 4
# 检查1
print(p.x, p.y)
# reset()
p.reset()
# 检查2
print(p.x, p.y)
# 输出为：
# 5 4
# 0 0

# 实例化一个对象pt
pt = Point()
# 给对象pt设定初始值
pt.x = 3
pt.y = 4
# 检查1
print(pt.x, pt.y)
# 在类中调用这个函数，并且明确地把这个对象作为self参数传给对象
Point.reset(pt)
# 检查2
print(pt.x, pt.y)

# 输出为：
# 3 4
# 0 0