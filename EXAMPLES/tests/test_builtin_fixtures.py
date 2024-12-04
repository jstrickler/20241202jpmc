import pytest

COUNTER_KEY = 'test_cache/counter'

def test_cache(cache):  # cache persists values between test runs
    value = cache.get(COUNTER_KEY, 0)
    print("Counter before:", value)
    cache.set(COUNTER_KEY, value + 1)  # cache fixture is similar to dictionary, but with .set() and .get() methods
    value = cache.get(COUNTER_KEY, 0)  # cache fixture is similar to dictionary, but with .set() and .get() methods
    print("Counter after:", value)
    assert True   # Make test successful

TEST_STRING = "Hello, pytesting world"

def hello():
    print(TEST_STRING)

def test_capsys(capsys):
    hello()  # Call function that writes text to STDOUT
    out, err = capsys.readouterr()  # Get captured output
    assert out.rstrip() == TEST_STRING

def bhello():
    print(b"Hello, binary pytesting world\n")

def test_capsysbinary(capsysbinary):
    bhello()  # Call function that writes binary text to STDOUT
    out, err = capsysbinary.readouterr()  # Get captured output
    print("BINARY STDOUT:", out)

def test_temp_dir1(tmpdir):
    print("TEMP DIR:", str(tmpdir))  # tmpdir fixture provides unique temporary folder name

def test_temp_dir2(tmpdir):
    print("TEMP DIR:", str(tmpdir))

def test_temp_dir3(tmpdir):
    print("TEMP DIR:", str(tmpdir))

if __name__ == '__main__':
    pytest.main([__file__, '-s', '-v'])   # Start the test runner