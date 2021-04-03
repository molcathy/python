import debugger
import pytest

def test_num_doubler():
    assert debugger.num_doubler([1, 2]) == [2, 4]
    assert debugger.num_doubler([-1, 0]) == [-2, 0]

def test_str_doubler():
    assert debugger.str_doubler(["a"]) == ["aa"]
    assert debugger.str_doubler(["a", "b"]) == ["aa", "bb"]
    assert debugger.str_doubler(["ddd", "cC"]) == ["dddddd", "cCcC"]
