# notebook.py
import datetime

# 为所有新的备注存储下一个可用的id
last_id = 0

class Note:
    '''
    notebook中的Note类。可以通过字符串搜索和存储每个Note
    '''

    def __init__(self, memo, tags=''):
        '''
        初始化，自动设置Note的创建日期和id
        :param memo:
        :param tags:
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''
        用filter匹配note的内容和标签，如果匹配到就返回True，否则返回False
        :param filter:
        :return:
        '''
        return filter in self.memo or filter in self.tags