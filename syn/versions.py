# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.


class Comparatron:
    _weights = {
        "~": -2,
        None: -1,
        "+": 1,
        ".": 2,
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
    delims = ["+", ".", "~"]
    v1s = _magic_strip(vid1, delims)
    v2s = _magic_strip(vid2, delims)

    def _normalize(a, b):
        fill = Comparatron(None)
        al = len(a)
        bl = len(b)
        delt = al - bl
        minval = al if al < bl else bl
        maxval = al if al > bl else bl
        if delt > 0:
            oper = b
        else:
            oper = a
        for i in range(minval, maxval):
            oper.append(fill)
        return a, b

    v1s, v2s = _normalize(v1s, v2s)

    for i in range(0, len(v1s)):
        v1 = v1s[i]
        v2 = v2s[i]
        if v1 != v2:
            return test(v1, v2)
    return None


def cmp_gt(vid1, vid2):
    def _gt(obj1, obj2):
        return obj1 > obj2
    return _do_compare(vid1, vid2, _gt) or False


def cmp_lt(vid1, vid2):
    def _lt(obj1, obj2):
        return obj1 < obj2
    return _do_compare(vid1, vid2, _lt) or False


def cmp_eq(vid1, vid2):
    def _shim(obj1, obj2):
        return False
    return _do_compare(vid1, vid2, _shim) == None
