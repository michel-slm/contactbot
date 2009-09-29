from abc import ABCMeta, abstractmethod
import os

CFG_DIR=os.path.join(os.getenv("HOME"),
                     ".config",
                     "hircus_contactbot")

class AbstractMicroBlog(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, id, password): pass

    @abstractmethod
    def get_messages(self): pass

    @abstractmethod
    def send_message(self, recpt, msg): pass

    @abstractmethod
    def friends_p(self, person1, person2): pass
