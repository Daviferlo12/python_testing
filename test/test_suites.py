import unittest
from test.test_bank_account import BankAccountTests
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def bank_acoount_suit():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests("test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    return suite
    
if __name__ == "__main__":  
    runner = unittest.TextTestRunner()
    runner.run(bank_acoount_suit())