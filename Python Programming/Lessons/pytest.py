import maths
import pytest


def test_add():
    assert maths.add(12, 24) == 36


def test_sub():
    assert maths.sub(24, 12) == 12
