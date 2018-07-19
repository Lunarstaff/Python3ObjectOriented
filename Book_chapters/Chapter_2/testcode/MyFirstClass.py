# MyFirstClass.py


# 定义一个什么都不做的类Point
class Point:
    pass


# 实例化两个对象
p1 = Point()
p2 = Point()

# 通过点记法给一个实例化的对象赋予任意属性
p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

# 检查对象的属性
print(p1.x, p1.y)
print(p2.x, p2.y)

# 输出为：
# 5 4
# 3 6
