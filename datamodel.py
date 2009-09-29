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

from storm.locals import *
import os

DB_BACKEND = 'sqlite:'
DB_FILE = os.path.join(os.getenv("HOME"),
                       ".config",
                       "hircus_contactbot",
                       "contacts.db")

DB_INITSQL = \
    """
CREATE TABLE person
  (id INTEGER PRIMARY KEY,
   screen_name VARCHAR,
   phone       VARCHAR,
   location    VARCHAR)       
"""

class Person(object):
    __storm_table__ = "person"
    id = Int(primary=True)
    screen_name = Unicode()
    phone = Unicode()
    location = Unicode()

class MsgDB(object):
    def __init__(self, db_backend=DB_BACKEND, db_file=DB_FILE):
        db_exists = db_file and os.path.exists(db_file)
        self.db = create_database(db_backend+db_file)
        self.store = Store(self.db)
        if not db_exists:
            # new database, needs initializing
            print "Initializing DB"
            self.store.execute(DB_INITSQL)
            print "DB initialized"
            self.store.flush()
            self.store.commit()

    def find_person(self, name):
        person = self.store.find(Person, \
                                 Person.screen_name == name).one()
        if not person:
            person = Person()
            person.screen_name = name
            self.store.add(person)

        return person
