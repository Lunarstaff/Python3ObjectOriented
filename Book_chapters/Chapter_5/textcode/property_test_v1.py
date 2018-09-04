# property_test.py
# 我们先装饰了foo方法，使它成为getter，然后用被装饰过的foo方法的setter属性又装饰了一个新方法
# 这个新方法的名字和刚才装饰过的foo方法是一样的。

class Foo:
    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value
