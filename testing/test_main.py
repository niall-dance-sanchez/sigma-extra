from main import add
import pytest


@pytest.mark.parametrize(("a", "b", "answer"), [
    (5, 5, 10),
    (-2, -4, -6),
    (0, 0, 0),
])
def test_basic(a, b, answer):
    assert add(a, b) == answer


@pytest.mark.parametrize(("a", "b"), [
    ("10", 5),
    (0.5, -4),
    ([10], 0),
])
def test_not_int(a, b):
    with pytest.raises(TypeError):
        add(a, b)
