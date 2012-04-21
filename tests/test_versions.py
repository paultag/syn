# $COPYRIGHT

from syn.versions import cmp_lt, cmp_gt, cmp_eq

def test_simple():
    v1 = "1"
    v2 = "2"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)


def test_minor():
    v1 = "1.0"
    v2 = "1.1"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)
    v1 = "1.0"
    v2 = "2.0"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)


def test_patch():
    v1 = "1.0.0"
    v2 = "1.0.1"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)
    v1 = "1.0.0"
    v2 = "1.1.0"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)
    v1 = "1.0.0"
    v2 = "2.0.0"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)


def test_plusthing():
    # test mismatched
    v1 = "1.0.0+1"
    v2 = "1.0.0.0"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)
    v1 = "1.0.0~1"
    v2 = "1.0.0+1"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)
    v1 = "1.0.0+1"
    v2 = "1.0.0+2"
    assert cmp_lt(v1, v2)
    assert cmp_gt(v2, v1)


def test_eqs():
    v1 = "1"
    v2 = "1"
    assert cmp_eq(v1, v2)
    v1 = "1.0"
    v2 = "1.0"
    assert cmp_eq(v1, v2)
    v1 = "1.0.0"
    v2 = "1.0.0"
    assert cmp_eq(v1, v2)
    v1 = "1.0.0+1~2"
    v2 = "1.0.0+1~2"
    assert cmp_eq(v1, v2)
