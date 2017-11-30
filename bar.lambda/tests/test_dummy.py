from src.MyFile import some_function


def test_dummy():
    assert True

def test_some_function():
    assert 'bailando' == some_function()
    assert 'helloWorld' != some_function()
