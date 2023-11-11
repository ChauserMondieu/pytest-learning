import textwrap
from math import sqrt
from pytest import approx


# assert value
def magnitude(x, y):
    return sqrt(x * x + y * y)


def get_long_class_description(class_name):
    assert class_name == "warrior"
    return textwrap.dedent(
        """\
        a seasoned veteran of many battles, High Strength and Dexterity allow to yield heavy armor and weapons, 
        as well as carry more equipment while keeping a light roll. Weak in magic.
        """
    )


def get_starting_equipment(class_name):
    assert class_name == "warrior"
    expected = ["long sword", "warrior weapon", "shield"]


def test_mag():
    assert magnitude(3, 4) == 5


def test_simple_math():
    assert abs(0.1 + 0.2) - 0.3 < 0.0001


def test_approx_simple():
    assert 0.1 + 0.2 == approx(0.3)


def test_approx_simple_fail():
    assert 0.1 + 0.2 == approx(0.35)


def test_warrior_long_class_description():
    desc = get_long_class_description("warrior")
    assert (
            desc
            == textwrap.dedent(
        """\
        a seasoned veteran of many battles, High Strength and Dexterity allow to yield heavy armor and weapons, 
        as well as carry more equipment while keeping a light roll. Weak in magic.
        """)
    )


def test_get_starting_equipment():
    expected = ["long sword", "warrior equipment"]
    assert get_starting_equipment() == expected, "wrong equipment"


def test_isinstance():
    task_id = 10
    assert isinstance(task_id, int)
