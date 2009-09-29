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

import datamodel

class MsgError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class MsgEval(object):
    def __init__(self, agent):
        self.__msg_db = datamodel.MsgDB()
        self.__agent = agent

    def eval(self, msg):
        sender = unicode(msg['sender_screen_name'])
        cmdtext = msg['text']
        cmds = cmdtext.split()

        if len(cmds) < 2:
            raise MsgError("Insufficient arguments")

        if cmds[0] == "set":
            cmds = cmds[1:]
            if len(cmds) < 2:
                raise MsgError("Invalid arguments: " + cmds)
            if cmds[0] == "phone":
                phone = unicode(cmds[1])
                person = self.__msg_db.find_person(sender)
                person.phone = phone
                self.__msg_db.store.flush()
                #return "new phone number for " + sender + " is " + cmds[1]
                return None
            elif cmds[0] == "location":
                location = unicode(cmdtext[cmdtext.index(cmds[1]):])
                person = self.__msg_db.find_person(sender)
                person.location = location
                self.__msg_db.store.flush()
                #return "new location for " + sender + " is " + location
                return None

            else:
                raise KeyError(cmds[0])
        elif cmds[0] == "phone":
            target = unicode(cmds[1])
            if sender==target or self.__agent.friends_p(target, sender):
                target_person = self.__msg_db.find_person(target)
                if target_person.phone:
                    return "%s can be reached at %s." \
                        % (target, target_person.phone)
                else:
                    return "%s has not left a number." \
                        % (target,)
            else:
                return "%s's phone number is on a need-to-know basis." \
                    % (target,)

        elif cmds[0] == "location":
            print "Got a location request!"
            target = unicode(cmds[1])
            if sender==target or self.__agent.friends_p(target, sender):
                target_person = self.__msg_db.find_person(target)
                if target_person.location:
                    return "%s is currently in %s." \
                        % (target, target_person.location)
                else:
                    return "%s's whereabout is unknown." \
                        % (target,)
            else:
                return "%s's whereabout is on a need-to-know basis." \
                    % (target,)
        else:
            raise KeyError(cmds[0])

    def quit(self):
        # commit remaining changes
        self.__msg_db.store.commit()
