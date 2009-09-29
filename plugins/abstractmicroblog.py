"""
Copyright (C) 2009 Michel Alexandre Sailm.  All rights reserved.

This file is part of Hircus ConnectBot.

Hircus ConnectBot is free software: you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Hircus ConnectBot is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with Hircus ConnectBot.  If not, see
<http://www.gnu.org/licenses/>.
"""

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
