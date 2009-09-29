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
import msg_eval

t = twitter.Twitter()

while True:
    # check if there is a request
    for m in t.get_messages():
        print m['sender_screen_name'], m['text']
        try:
            result = msg_eval.eval(m)
        except Exception as e:
            result = str(type(e)) + ": " + str(e)
        t.send_message(m['sender_screen_name'], result)

    time.sleep(30)

