# MySubClassv4_0.py
# AudioPlay

"""
所有音频文件的检查确保了初始化的一个有效扩展
多态可以让父类的init方法去访问来自不同子类的ext类变量。
"""

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):     # 如果文件名不是以指定的后缀名结尾
            raise Exception("Invalid file format")  # 弹出异常“Invalid file format(文件格式不合法)”

        self.filename = filename


# MP3文件子类
class MP3File(AudioFile):
    ext = "mp3" # 文件后缀名为“mp3”

    def play(self):
        print("Playing {} as mp3".format(self.filename))


# wav文件子类
class WavFile(AudioFile):
    ext = "wav" # 文件后缀名为“wav”

    def play(self):
        print("Playing {} as wav".format(self.filename))


# ogg文件子类
class OggFile(AudioFile):
    ext = "ogg" # 文件后缀名为“ogg”

    def play(self):
        print("Playing {} as ogg".format(self.filename))