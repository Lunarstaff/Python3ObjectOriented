# Property.py


class Property:
    """
        房产类型：
        Property（房产）
            面积
            卧室及浴室的数量
    """
    # 因为要在多重继承里使用Property类，给init方法额外添加了**kwargs参数
    # kwargs：关键字参数keyword args
    def __init__(self, square_m="", beds="", baths="", **kwargs):
        """
        初始化方法：
        :param square_m: 面积（单位：m^2）
        :param beds:        卧室数量
        :param baths:       浴室数量
        :param kwargs:      其他
        """
        # 为避免在多重继承中我们不是最后一个调用，包含了调用super().__init__方法
        super().__init__(**kwargs)
        self.square_m = square_m
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        输出信息方法：
        打印房产的面积、卧室数量、浴室数量等信息。
        :return:
        """
        print("房产详情：")
        print("=======================")
        print("面积为：{}\tm^2".format(self.square_m))
        print("卧室数量为：{}\t个".format(self.num_bedrooms))
        print("浴室数量为：{}\t个".format(self.num_baths))
        print()

    # prompt_init() 方法设置成为静态方法
    # 静态方法只和一个类（就像类的变量）关联，而不是和一个具体的对象实例，所以没有self参数
    def prompt_init():
        return dict(square_m=input("请输入面积（单位：m^2）:"),
                    beds=input("请输入卧室数量（单位：个）："),
                    baths=input("请输入浴室数量（单位：个）："))
    prompt_init = staticmethod(prompt_init)


# Apartment类继承自Property类
class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")   # 洗衣间信息枚举
    valid_balconies = ("yes", "no", "solarium")     # 阳台信息枚举

    def __init__(self, balcony="", laundry="", **kwargs):
        # init方法通过调用父类的init方法确保Property类正确地被初始化
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    # 重写display()方法
    def display(self):
        # display()方法通过调用父类的display()方法确保Property类正确地被初始化
        super().display()
        print("公寓详细信息")
        print("洗衣间信息：" + self.laundry)
        print("阳台信息：" + self.balcony)

        # 使用父类Property的静态方法产生的字典
        parent_init = Property.prompt_init()
        laundry = ""
        while laundry.lower() not in Apartment.valid_laundries:
            # 提示输入洗衣间信息并展示洗衣间信息枚举
            laundry = input("请输入洗衣间的属性（{}）：".format(", ".join(Apartment.valid_laundries)))

        balcony = ""
        while balcony.lower() not in Apartment.valid_balconies:
            # 提示输入阳台信息并展示阳台信息枚举
            balcony = input("请输入阳台的属性（{}）：".format(", ".join(Apartment.valid_balconies)))

        # dict.update方法把新的字典值合并到第一个字典里
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    # 声明prompt_init为静态方法，一个文件只需要一条这样的语句
    # prompt_init = staticmethod(prompt_init)
