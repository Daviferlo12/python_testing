import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
        
    def add_account(self, account):
        self.accounts.append(account)
        
    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)
