from hermes_langlib import check_for_update


def test_updates():
    assert check_for_update()
