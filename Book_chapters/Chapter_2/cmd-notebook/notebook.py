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

class Notebook:
    """
    notes的收集，可以用标签管理，修改，查询
    """
    def __init__(self):
        """
        用一个空的列表初始化Notebook
        """
        self.notes = []

    def new_note(self, memo, tags=""):
        """
        创建一个新的note并添加到列表中
        :param memo:
        :param tags:
        :return:
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        找到notebook中指定id的note
        :param note_id:
        :return:
        """
        for note in self.notes:
            if str(note.id) ==  (note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        修改指定id的note的内容
        :param note_id:
        :param memo:
        :return:
        """
        # v1.0
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.memo = memo
        #         break

        # v2.0
        # self._find_note(note_id).memo = memo

        # v3.0
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """
        修改指定id的note的标签
        :param mote_id:
        :param tags:
        :return:
        """

        # v1.0
        # for note in self.notes:
        #     if note.id == note_id:
        #         note.tags = tags
        #         break

        # v2.0
        self._find_note(note_id).tags = tags

    def search(self, filter):
        """
        根据filter查找所有的note
        :param filter:
        :return:
        """
        # return [note for note in self.notes if note.match(filter)]
        search_ls = []
        for note in self.notes:
            if note.match(filter):
                search_ls.append(note)
        return search_ls

