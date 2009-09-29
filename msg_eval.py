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

class MsgError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def eval(msg):
    sender = msg['sender_screen_name']
    cmdtext = msg['text']
    cmds = cmdtext.split()

    if len(cmds) < 2:
        raise MsgError("Insufficient arguments")

    if cmds[0] == "set":
        cmds = cmds[1:]
        if len(cmds) < 2:
            raise MsgError("Invalid arguments: " + cmds)
        if cmds[0] == "phone":
            return "new phone number for " + sender + " is " + cmds[1]
        elif cmds[0] == "location":
            return "new location for " + sender + " is " + \
                cmdtext[cmdtext.index(cmds[1]):]

        else:
            raise KeyError(cmds[0])
    elif cmds[0] == "phone":
        raise NotImplementedError()
    elif cmds[0] == "location":
        raise NotImplementedError()
    else:
        raise KeyError(cmds[0])


            
