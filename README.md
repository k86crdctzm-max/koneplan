# コネプラ

小さな練習用プロジェクトです。初めての Pull Request を体験するために作りました。

## 機能

- `greet(name)`: 名前を受け取って、あいさつ文を返します。
- `add(a, b)`: 2 つの数値を受け取って、その合計を返します。

## 使い方

```python
from greeting import greet, add

print(greet("世界"))   # こんにちは、世界さん!
print(add(2, 3))        # 5
```

## テストの実行

```bash
python -m pytest
```
