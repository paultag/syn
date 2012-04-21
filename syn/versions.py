# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

class Comparatron:
    _weights = {
        "~" : -1,
        "+" : 1,
        "." : 2,
    }
    def __init__(self, string):
        self.string = string

    def _get_weight(self):
        return self._weights[self.string]

    def __lt__(self, other):
        return self._get_weight() < other._get_weight()

    def __gt__(self, other):
        return self._get_weight() > other._get_weight()

    def __ne__(self, other):
        return self._get_weight() != other._get_weight()

    def __eq__(self, other):
        return self._get_weight() == other._get_weight()

    def __ge__(self, other):
        return self._get_weight() >= other._get_weight()

    def __le__(self, other):
        return self._get_weight() <= other._get_weight()


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


def _do_compare(vid1, vid2, test):
    """Is none true or false?"""
    delims = [ "+", ".", "~" ]
    v1s = _magic_strip(vid1, delims)
    v2s = _magic_strip(vid2, delims)

    for i in range(0, len(v1s)):
        v1 = v1s[i]
        v2 = v2s[i]
        if v1 != v2:
            return test(v1, v2)
    return None


def cmp_lt(vid1, vid2):
    def _lt(obj1, obj2):
        return obj1 < obj2
    return _do_compare(vid1, vid2, _lt)


def cmp_gt(vid1, vid2):
    def _gt(obj1, obj2):
        return obj1 > obj2
    return _do_compare(vid1, vid2, _gt)


def cmp_eq(vid1, vid2):
    def _shim(obj1, obj2):
        return False
    return _do_compare(vid1, vid2, _shim) == None
