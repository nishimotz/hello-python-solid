class Money:
    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency
        
    @property
    def amount(self) -> int:
        return self._amount
        
    @property
    def currency(self) -> str:
        return self._currency
        
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency
        
    def __repr__(self) -> str:
        return f"Money({self.amount}, '{self.currency}')"