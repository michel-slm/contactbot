from abstractmicroblog import AbstractMicroBlog, CFG_DIR
from twyt import twitter as _twitter
import simplejson
import os, sys

TWITTER_CFG = os.path.join(CFG_DIR, "twitter.conf")

class Twitter(AbstractMicroBlog):

    def __init__(self, account=None, passwd=None):
        self.__t = _twitter.Twitter()
        if account==None and passwd==None:
            # let it throw IOError if file is not found
            with open(TWITTER_CFG, 'r') as f:
                self.__conf = simplejson.load(f)
        elif account and passwd:
            self.__conf = {"account": account,
                           "password": passwd,
                           "lastmsg_id": None,
                           }
            with open(TWITTER_CFG, 'w') as f:
                simplejson.dump(self.__conf, f)
        else:
            raise TypeError("%s cannot be null",
                            ("account" if passwd else "passwd",))
        self.__account = self.__conf["account"]
        self.__t.set_auth(self.__account, self.__conf["password"])

        """
        Sanity check.
        twyt does not actually check if authentication succeeds or not
        """
        try:
            self.__t.direct_sent(1)
        except _twitter.TwitterException:
            sys.exit("Unable to authenticate. Check config file")

    def get_messages(self):
        try:
            msgs = simplejson.loads(
                self. __t.direct_messages(since_id=self.__conf['lastmsg_id']))
        except _twitter.TwitterException:
            # This is likely a transient error
            return []
        
        if msgs:
            self.__conf['lastmsg_id'] = msgs[0]['id']
            # Persist changed lastmsg_id to disk
            with open(TWITTER_CFG, 'w') as f:
                simplejson.dump(self.__conf, f)
        return msgs

    def send_message(self, recpt, msg):
        return self.__t.direct_new(recpt, msg)

    def friends_p(self, person1, person2):
        return self.__t.friendship_exists(person1, person2)
