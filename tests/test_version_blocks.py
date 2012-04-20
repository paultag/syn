# $COPYRIGHT_NOTICE


from syn.versions import VersionBlock

def test_basic_cmp():
    vb1 = VersionBlock("1")
    vb2 = VersionBlock("2")
    assert vb2 > vb1
