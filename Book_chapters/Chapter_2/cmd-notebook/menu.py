# menu.py
import sys
from notebook import Notebook, Note

class Menu:
    """
    运行时显示菜单，并响应输入选择
    """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu
        
        1.Show all Notes（显示所有的记录）
        2.Search Notes（查找笔记）
        3.Add Note（添加一条笔记）
        4.Modify Note（修改一条笔记）
        5.Quit（退出）
        """)

    def run(self):
        """
        显示菜单、响应选择
        :return:
        """
        while True:
            self.display_menu()
            choice = input("请输入功能选项：")
            action = self.choices.get(choice) # choices 是个字典
            if action:
                action()
            else:
                print("没有{}选项，请重新输入！".format(choice))

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}:{1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("请输入要查找的关键字：")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("请输入笔记：")
        self.notebook.new_note(memo)
        print("笔记添加成功！")

    def modify_note(self):
        id = input("请输入要修改的笔记ID：")
        # 这里需要查询反显原笔记内容
        memo = input("请输入修改后的内容：")
        tags = input("请输入要保存为的标签：")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("谢谢使用cmd-notebook，再见！")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
