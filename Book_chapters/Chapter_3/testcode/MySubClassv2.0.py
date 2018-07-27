# MySubClassv2.0.py

# 扩展内置类，给列表类扩展，添加一个方法用于搜索
class ContactList(list):
    def search(self, name):
        """
        返回通过name查找到的contacts，列表类
        :param name:
        :return:
        """
        matching_contacts = [] # 查找结果
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    """
    一个通讯录类
    """
    all_contacts = ContactList()
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


# 创建一个新的叫Supplier的类，和Contact类一样，但是他有额外的order(订单)方法
class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send {} order to {}".format(order, self.name))
