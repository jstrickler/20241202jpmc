import pytest

from jpmcutil import sample_function
from jpmcutil import Jpmcutil

@pytest.fixture
def Jpmcutil_object():
    obj = Jpmcutil()
    return obj

def test_Jpmcutil_instance_has_sample_method(Jpmcutil_object):
    assert hasattr(Jpmcutil_object, "sample_method")

def test_jpmcutil_has_sample_function():
    assert sample_function() is None  # no return value
