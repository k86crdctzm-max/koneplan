"""greeting モジュールのテスト。"""

from greeting import greet, add


def test_greet():
    assert greet("世界") == "こんにちは、世界さん!"


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
