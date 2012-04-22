# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

from syn.db import Database
from nose.tools import with_setup

db_name = ".removeme.db"

def test_basic_rw():
    db = Database(db_name)
    db.clear()
    db.sync()
    db['foo'] = "bar"
    assert db['foo'] == "bar"
    db.sync()
    db = None
    db = Database(db_name)
    assert db['foo'] == "bar"
