"""greeting モジュールのテスト。"""

from greeting import greet


def test_greet():
    assert greet("世界") == "こんにちは、世界さん!"
