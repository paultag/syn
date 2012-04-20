# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

class Comparatron:
    _weights = {
        "~" : -1,
        "." : 0,
        "+" : 1
    }
    def __init__(self, string):
        self.string = string

    def _get_weight(self):
        return self._weights[self.string]

    def __lt__(self, other):
        return self._get_weight < other._get_weight

    def __gt__(self, other):
        return self._get_weight > other._get_weight

    def __eq__(self, other):
        return self._get_weight == other._get_weight

    def __ge__(self, other):
        return self._get_weight >= other._get_weight

    def __le__(self, other):
        return self._get_weight <= other._get_weight


def _magic_strip(string, tokens):
    ret = []
    buf = ""
    for char in string:
        if char in tokens:
            ret.append(buf)
            ret.append(Comparatron(char))
            buf = ""
            continue
        buf += char
    ret.append(buf)
    return ret

def _do_compare(vid1, vid2):
    delims = [ "+", ".", "~" ]
    vid1s = _magic_strip(vid1, delims)
    vid2s = _magic_strip(vid2, delims)

    for x in range(0, len(vid1s)):
        if vid1s[x] != vid2s[x]:
            return vid1s[x] > vid2s[x]

class VersionBlock:
    def __init__(self, version_string):
        self._vs = version_string

    def __get_vs(self):
        return self._vs

    def __gt__(self, other):
        cp = _do_compare(self._vs, other.__get_vs)
        return cp == 1

class Version:
    def __init__(self, version_string):
        self._vs = version_string
