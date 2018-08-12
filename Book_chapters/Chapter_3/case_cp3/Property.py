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
        # v1.0
        # laundry = ""
        # while laundry.lower() not in Apartment.valid_laundries:
        #     # 提示输入洗衣间信息并展示洗衣间信息枚举
        #     laundry = input("请输入洗衣间的属性（{}）：".format(", ".join(Apartment.valid_laundries)))
        #
        # balcony = ""
        # while balcony.lower() not in Apartment.valid_balconies:
        #     # 提示输入阳台信息并展示阳台信息枚举
        #     balcony = input("请输入阳台的属性（{}）：".format(", ".join(Apartment.valid_balconies)))

        # 根据v1.0中的处理方法，提取出get_valid_input方法，将v1.0优化如下：
        # V2.0
        laundry = get_valid_input("请输入洗衣间的属性:", Apartment.valid_laundries)
        balcony = get_valid_input("请输入阳台的属性：", Apartment.valid_balconies)

        # dict.update方法把新的字典值合并到第一个字典里
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    # 声明prompt_init为静态方法，一个类需要一条这样的语句
    # prompt_init = staticmethod(prompt_init)


# 编写一个测试方法,把上面v1.0的交互方式提取出来
def get_valid_input(input_string, valid_options):
    """
    传入两个参数，输入提示语（字符串类）和属性枚举（元组类）。
    :param input_string:
    :param valid_options:
    :return:
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response

# 根据上面这个验证方法，修改Apartment.prompt_init方法, 如上v2.0


# House类，继承自Property类，与Apartment类平行
class House(Property):
    valid_garage = ("attached", "detached", "none")     # 停车位信息枚举
    valid_fenced = ("yes", "no")                        # 围墙信息枚举

    def __init__(self, num_stories="", garage="", fenced="", **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories  # House的仓库数量

    def display(self):
        super().display()
        print("House信息详情：")
        print("仓库的数量为：{}".format(self.num_stories))
        print("车位信息：{}".format(self.garage))
        print("围墙信息：{}".format(self.fenced))

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("请输入围墙信息：", House.valid_fenced)
        garage = get_valid_input("请输入车位信息：", House.valid_garage)
        num_stories = input("请输入仓库数量：")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return  parent_init
    # 声明静态方法：
    prompt_init = staticmethod(prompt_init)

# Purchase 购置类
class Purchase:
    def __init__(self, price="", taxes="", **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super.display()
