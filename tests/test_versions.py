# $COPYRIGHT

from syn.versions import cmp_lt, cmp_gt, cmp_eq


def test_less_then():
    v1 = "1"
    v2 = "2"
    assert cmp_lt(v1, v2)
    v1 = "1.0"
    v2 = "1.1"
    assert cmp_lt(v1, v2)
    v1 = "1.0.0"
    v2 = "1.0.1"
    assert cmp_lt(v1, v2)
    v1 = "1~1"
    v2 = "1.0"
    assert cmp_lt(v1, v2)
    v1 = "1+0"
    v2 = "1.1"
    assert cmp_lt(v1, v2)
    v1 = "1~1"
    v2 = "1+1"
    assert cmp_lt(v1, v2)
    v1 = "1"
    v2 = "1+1"
    assert cmp_lt(v1, v2)
    v1 = "1+1"
    v2 = "1+2"
    assert cmp_lt(v1, v2)


def test_greater_then():
    v1 = "1"
    v2 = "2"
    assert cmp_gt(v2, v1)
    v1 = "1.0"
    v2 = "1.1"
    assert cmp_gt(v2, v1)
    v1 = "1.0.0"
    v2 = "1.0.1"
    assert cmp_gt(v2, v1)
    v1 = "1~1"
    v2 = "1.0"
    assert cmp_gt(v2, v1)
    v1 = "1+0"
    v2 = "1.1"
    assert cmp_gt(v2, v1)
    v1 = "1~1"
    v2 = "1+1"
    assert cmp_gt(v2, v1)
    v1 = "1"
    v2 = "1+1"
    assert cmp_gt(v2, v1)
    v1 = "1+1"
    v2 = "1+2"
    assert cmp_gt(v2, v1)


def test_eq():
    v1 = "1.0"
    v2 = "1.0"
    assert cmp_eq(v1, v2)
    assert cmp_lt(v1, v2) == False
    assert cmp_gt(v1, v2) == False
