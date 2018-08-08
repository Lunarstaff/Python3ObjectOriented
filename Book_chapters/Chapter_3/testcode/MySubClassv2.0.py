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


# Friend类，从Contact类继承，继承时重写init方法
# v1.0，直接根据原方法重写
# class Friend(Contact):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

# v2.0，调用父类的方法，进行重写
class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


# 一个mixin类
class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # 电子邮件发送的实现


# 通过多重继承定义一个新的类，既是Contact类 又是MailSender类
class EmailableContact(Contact, MailSender):
    pass


# 增加一个存放地址的类：AddressHolder
class AddressHolder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


# Friend类 v3.0
class Friend(Contact, AddressHolder):
    """
    直接调用了每一个超类的init方法并且显示地传递了self参数。

    Friend类的init方法首先调用了Contact类的init方法，隐式初始化了Object超类
    Friend类然后调用了AddressHolder类的init方法，又一次隐式初始化了Object超类。
    问题就在于父类被创建了两次，这不是我们期待的行为，并且如果这个方法正在做实际的工作，
    这将导致非常严重的bug，像往一个银行账户存款两次一样！
    """
    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self,name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone

