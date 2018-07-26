# MySubClassv1.0.py
class Contact:
    """
    一个通讯录类
    """
    all_contacts = []
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


# 创建一个新的叫Supplier的类，和Contact类一样，但是他有额外的order(订单)方法
class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send {} order to {}".format(order, self.name))
