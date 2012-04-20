# Copyright (c) Syn AUTHORS, 2012, under the terms and conditions of the
# AUTHORS file.

from syn.versions import Version

def test_simple():
    v1 = Version("1")
    v2 = Version("2")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2


def test_eq():
    v1 = Version("1")
    v2 = Version("1")
    assert v1 == v2


def test_major_minor():
    v1 = Version("1.0")
    v2 = Version("2.0")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
    # Ensure we block it out right.
    v1 = Version("1.0")
    v2 = Version("1.1")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2


def test_major_minor_patch():
    v1 = Version("1.0.0")
    v2 = Version("2.0.0")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
    # Ensure we block it out right.
    v1 = Version("1.0.0")
    v2 = Version("1.1.0")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
    # Ensure we block it out right.
    v1 = Version("1.0.0")
    v2 = Version("1.0.1")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2


def test_greater_thinger():
    v1 = Version("1")
    v2 = Version("2+1")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
    v1 = Version("1")
    v2 = Version("1+1")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
    v1 = Version("1+1")
    v2 = Version("1.0")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2


def test_lessthen_thinger():
    v1 = Version("1~1")
    v2 = Version("1")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
    v1 = Version("1~1")
    v2 = Version("1.0")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
    v1 = Version("0.0")
    v2 = Version("1~1")
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2
