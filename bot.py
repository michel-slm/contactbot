#!/usr/bin/env python
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

from plugins import twitter
import os, sys, time
from msg_eval import MsgEval
import datamodel

t = twitter.Twitter()
msg_eval = MsgEval(t)

try:
    while True:
        # check if there is a request
        # reverse the list, due to reverse chronological order
        # to make sure later commands overwrite earlier ones
        for m in t.get_messages()[::-1]:
            sys.stdout.write(m['sender_screen_name'] + ": " + m['text'] + "\n")
            try:
                result = msg_eval.eval(m)
            except Exception as e:
                result = str(type(e)) + ": " + str(e)
            if result:
                print result
                t.send_message(m['sender_screen_name'], result)
            else:
                sys.stdout.write("Message processed silently.\n")

        time.sleep(30)

except KeyboardInterrupt as e:
    sys.stdout.write("Quitting\n")
    msg_eval.quit()

