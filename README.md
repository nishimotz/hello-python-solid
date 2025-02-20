# FizzBuzz with SOLID Principles

SOLIDの原則に基づいたFizzBuzzをAIに実装してもらった例です。

## 設計のポイント

### 抽象基底クラス `Rule`

```python
class Rule(ABC):
    @abstractmethod
    def apply(self, number: int) -> str:
        pass
```

- 単一の抽象メソッド `apply` を持つ
- 入力は整数値、出力は文字列
- 空文字を返すことで、ルールが適用できない場合を表現

### 具象クラス群

各ルールは独立した責任を持ち、`Rule` を実装します：

1. `FizzBuzzRule`: 15の倍数を判定
2. `FizzRule`: 3の倍数を判定
3. `BuzzRule`: 5の倍数を判定
4. `NumberRule`: デフォルトの数値変換

### ルール適用クラス `FizzBuzzProcessor`

```python
class FizzBuzzProcessor:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
```

- ルールのリストを受け取り、順番に適用
- ルールの順序が処理の優先順位を決定
- 新しいルールの追加が容易

## SOLIDの原則との対応

1. 単一責任の原則 (SRP)
   - 各ルールクラスは1つの変換ルールのみを担当
   - プロセッサーはルールの適用に専念

2. オープン・クローズドの原則 (OCP)
   - 新しいルールの追加は `Rule` を実装するだけ
   - 既存コードの修正は不要

3. リスコフの置換原則 (LSP)
   - すべてのルールは `Rule` インターフェースを完全に満たす
   - ルール間で一貫した入出力型を保持

4. インターフェース分離の原則 (ISP)
   - `Rule` は必要最小限のメソッドのみを定義
   - 余分なメソッドを強制しない

5. 依存性逆転の原則 (DIP)
   - プロセッサーは具象クラスではなく `Rule` に依存
   - ルールの注入により柔軟な構成が可能

## テストと型チェック

```bash
uv venv
uv pip install -r requirements.txt
uv run pytest
uv run mypy fizzbuzz.py test_fizzbuzz.py
```

## 実行

```bash
uv run fizzbuzz.py
```
