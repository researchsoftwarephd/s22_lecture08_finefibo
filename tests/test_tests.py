import pytest

# def test_will_fail():
#     assert 1 < 0

@pytest.mark.skip()
def test_will_be_skipped():
    assert 1 == 1

@pytest.mark.xfail()
def test_will_fail_as_expected():
    assert 1 < 0

@pytest.mark.xfail()
def test_will_pass_but_not_supposed_to():
    assert 1 > 0

def test_the_meaning_of_life(meaning_of_life):
    assert meaning_of_life == 42

@pytest.mark.xfail()
def test_not_meaningful(meaning_of_life):
    assert meaning_of_life == 24

