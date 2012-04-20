# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

import json

class Database(dict):
    def __init__(self, fil):
        self._file = fil

    def load(self):
        db = json.load(open(self._file, 'r'))
        for item in db:
            self[item] = db[item]

    def sync(self):
        open(self._file, 'w').write(json.dumps(self))
