import pytest
from fizzbuzz import Rule, FizzRule, BuzzRule, FizzBuzzRule, NumberRule, FizzBuzzProcessor

def test_rule_is_abstract():
    # Rule クラスは直接インスタンス化できないことを確認
    with pytest.raises(TypeError):
        Rule()

def test_rule_has_apply_method():
    # Rule クラスが apply メソッドを持つことを確認
    assert hasattr(Rule, 'apply')

def test_fizz_rule():
    rule = FizzRule()
    assert rule.apply(3) == "Fizz"
    assert rule.apply(6) == "Fizz"
    assert rule.apply(5) == ""  # Fizz のルールに該当しない場合

def test_buzz_rule():
    rule = BuzzRule()
    assert rule.apply(5) == "Buzz"
    assert rule.apply(10) == "Buzz"
    assert rule.apply(3) == ""  # Buzz のルールに該当しない場合

def test_fizzbuzz_rule():
    rule = FizzBuzzRule()
    assert rule.apply(15) == "FizzBuzz"
    assert rule.apply(30) == "FizzBuzz"
    assert rule.apply(3) == ""  # FizzBuzz のルールに該当しない場合

def test_number_rule():
    rule = NumberRule()
    assert rule.apply(1) == "1"
    assert rule.apply(2) == "2"
    assert rule.apply(4) == "4"

def test_fizzbuzz_processor():
    # ルールの優先順位: FizzBuzz > Fizz > Buzz > Number
    processor = FizzBuzzProcessor([
        FizzBuzzRule(),
        FizzRule(),
        BuzzRule(),
        NumberRule()
    ])
    
    # 通常の数字の場合
    assert processor.process(1) == "1"
    assert processor.process(2) == "2"
    assert processor.process(4) == "4"
    
    # Fizz の場合
    assert processor.process(3) == "Fizz"
    assert processor.process(6) == "Fizz"
    
    # Buzz の場合
    assert processor.process(5) == "Buzz"
    assert processor.process(10) == "Buzz"
    
    # FizzBuzz の場合（15の倍数）
    assert processor.process(15) == "FizzBuzz"
    assert processor.process(30) == "FizzBuzz"
