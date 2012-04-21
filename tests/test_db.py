# $COPYRIGHT

from syn.db import Database
from nose.tools import with_setup

db_name = "testting.db"

def test_basic_rw():
    db = Database(db_name)
    db.load()
    db.clear()
    db.sync()
    db['foo'] = "bar"
    assert db['foo'] == "bar"
    db.sync()
    db = None
    db = Database(db_name)
    db.load()
    assert db['foo'] == "bar"
