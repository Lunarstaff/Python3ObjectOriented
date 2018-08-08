# MySubClassv3_0.py

# Contact类：
class Contact:
    all_contacts = []
    def __init__(self, name="", email="", **kwargs):
        """
        通过设置空字符为参数默认值，
        也包含了一个 **kwargs参数，可以捕获任何特殊方法不知道如何处理的额外参数
        :param name:
        :param email:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


# AddressHolder类：
class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


# Friend类：
class Friend(Contact, AddressHolder):
    def __init__(self, phone ="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone