import pytest

from hypothesis import given
from hypothesis.strategies import integers, composite


@given(integers(max_value=12345678))
def test_some_method(var):
    assert var <= 12345678


if __name__ == '__main__':
    pytest.main()
