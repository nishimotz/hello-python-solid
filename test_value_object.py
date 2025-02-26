from value_object import Money
import pytest

def test_money_value_object():
    # Money値オブジェクトの作成
    yen1000 = Money(1000, 'JPY')
    assert yen1000.amount == 1000
    assert yen1000.currency == 'JPY'

    another_yen1000 = Money(1000, 'JPY')
    assert another_yen1000.amount == 1000
    assert another_yen1000.currency == 'JPY'

    usd10 = Money(10, 'USD')
    assert usd10.amount == 10
    assert usd10.currency == 'USD'

    # 値ベースの比較
    assert yen1000 == another_yen1000
    assert yen1000 != usd10

    # 不変性の確認
    with pytest.raises(AttributeError):
        yen1000.amount = 2000  # AttributeErrorが発生
