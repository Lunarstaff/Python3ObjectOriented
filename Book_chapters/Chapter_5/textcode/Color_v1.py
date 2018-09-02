# 使用Python中的property关键字，使一个方法看起来就像一个属性一样。
class Color:
    """
    1、将name属性设置为一个（半）私有的_name属性，
    2、添加两个（半）私有方法对这个_name进行取值和赋值，并在赋值时进行验证。
    3、在代码底部使用property关键字进行声明

    name属性变成了一个property属性，需要通过调用添加的两个（半）私有方法才能访问或是改变其值。
    """
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)
