import pytest

@pytest.fixture(scope = "module")
def meaning_of_life():
    return 42