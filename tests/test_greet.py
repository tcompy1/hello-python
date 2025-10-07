from hello.main import greet


def test_greet():
    assert greet("Trent") == "Hello, Trent!"
