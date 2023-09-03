from utils.dicts import get_val


def test_get_val():
    assert get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert get_val({"vcs": "mercurial", "vcs2": "bazaar"}, "vcs") == "mercurial"
    assert get_val({"vcs": "mercurial", "vcs2": "bazaar"}, None) == "git"
    assert get_val({}, None) == "git"
    assert get_val({}, None, "collab") == "collab"
