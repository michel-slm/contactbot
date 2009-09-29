#!/usr/bin/env python
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

