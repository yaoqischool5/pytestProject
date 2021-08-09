import pytest


def add(x,y):
    return x+y

def test_add():
    assert add(1,10) ==11
    assert add(1,1)==2
    assert add(1,9)==8
    print("输出结果")

class TestClass:
    @pytest.mark.test
    def test_one(self):
        x="this"
        assert "h" in x
        print("输出结果")
    @pytest.mark.test
    def test_two(self):
        x="hello"
        assert hasattr(x,"check")