import pytest

def test_two_plus_two_equals_four():  # tests should begin with "test" (or will not be found automatically)
    assert 2 + 2 == 4   # if assert statement succeeds, the test passes
    assert 3 + 3 == 6
    
def test_empty_string_has_length_zero():
    print("Hi Mom!")
    assert len("") == 0

def wombats():
    print("wombats!")

if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner