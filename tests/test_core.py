import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目: 
#
# 1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
# 2. 下一步提款 500 元, 確認帳戶總金額為 600 元
# 3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
# 4.之後提款 700 元, pytest 預期會接到 RuntimeError
#
##########################################################################################
    customer = Customer('Test User', '100-1100')
    customer.deposit(INIT_MONEY)

    def test_deposit(self):
        self.customer.deposit(1000)
        assert(self.customer.balance == 1100)

    def test_withdraw(self):
        self.customer.withdraw(500)
        assert(self.customer.balance == 600)

    def test_add_interest(self):
        CustomerDataProcess.add_interest(self.customer, 0.1)
        assert(round(self.customer.balance,0) == 660)

    def test_over_withdraw(self):
        self.customer.withdraw(700)

    
    


