__import__("bank.py")
import itertools


class hold(object):
    pass


class acct(dict):
    """An authorized account within which transaction are made"""
    def newid():
        itertools.count()

    def __init__(self, bal, lines=[], name = None):
        """

        :type bal: object
        """
        if name is None:
            return ValueError('You need to give your account a name')

        self.id = acct.newid()
        assert isinstance(bal, float)
    self.bal = bal

    def deposit(self, input):
        self.balance += input

    def withdraw(self, input):
        self.balance -= input  
    def overdrawn(self):
        return self.balance < 0

    def tran(transaction, amount, category):
        account.balance += amount
        """here, we want to have some sort of transaction from a LIneItem Object for the account"""
        account.line = []


class LineItems:
    pass


class transaction(object):
    """A withdrawal or deposit; creates at least one line item"""
    def __init__(self, account, amount, category=None):
        self.account += amount
