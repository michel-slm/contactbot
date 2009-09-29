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


            
