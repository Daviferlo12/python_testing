import sys
import os
import unittest
from unittest.mock import patch, MagicMock
from src.bank_account import BankAccount
from src.exceptions import WithdrawalTimeRestrictionError, InsuficientFoundError, WithdrawalWeekendRestriccion

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class BankAccountTests(unittest.TestCase):
    
    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
    
    def test_deposit(self):
        self.assertEqual(self.account.deposit(500), 1500, "El balance no es igual") 
    
    @patch("src.bank_account.datetime")
    def test_withdraw(self, mock_datetime):
        mock_today = MagicMock()
        mock_today.weekday.return_value = 1
        mock_today.hour = 4
        mock_datetime.now.return_value = mock_today
        self.assertEqual(self.account.withdraw(500), 500, "El balance no es igual")
           
    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000, "El balance no es igual")

    def test_transaccion_log(self):
        self.assertTrue(os.path.exists("transaction_log.txt"), "No se crea el log correctamente")
                
    def _count_lines(self, file_name):
        with open(file_name, "r") as f:
            return len(f.readlines())
        
    def test_count_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1, "El numero de lineas no es igual")
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2, "El numero de lineas no es igual")
        
    def test_transfer(self):
        other_account = BankAccount(balance=2000, log_file="other_account_log.txt")
        self.assertEqual(self.account.transfer(200, other_account), 800, "El balance no es igual")
    
    def test_transfer_raise_error_not_suficient_money(self):
        with self.assertRaises(ValueError):
            other_account = BankAccount(balance=2000, log_file="other_account_log.txt")
            self.account.transfer(2000, other_account)
    
    def test_withdraw_raises_error_when_insuficient_funds(self):
        with self.assertRaises(InsuficientFoundError):
            self.account.withdraw(3000)
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_today = MagicMock()
        mock_today.weekday.return_value = 1
        mock_today.hour = 10
        mock_datetime.now.return_value = mock_today
        self.assertEqual(self.account.withdraw(200), 800, "El balance no es igual")
        
        
    @patch("src.bank_account.datetime")
    def test_withdraw_raises_error_when_outof_bussines_hours(self, mock_datetime):
        mock_today = MagicMock()
        mock_today.weekday.return_value = 1
        mock_today.hour = 20 
        mock_datetime.now.return_value = mock_today
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(200)
            
    @patch("src.bank_account.datetime")
    def test_withdraw_during_available_day(self, mock_datetime):
        mock_today = MagicMock()
        mock_today.weekday.return_value = 4
        mock_today.hour = 10 
        mock_datetime.now.return_value = mock_today
        self.assertEqual(self.account.withdraw(200), 800, "El balance no es igual")
        
    @patch("src.bank_account.datetime")
    def test_withdraw_raise_error_when_unavailable_day(self, mock_datetime):
        mock_today = MagicMock()
        mock_today.weekday.return_value = 5
        mock_today.hour = 10 
        mock_datetime.now.return_value = mock_today
        with self.assertRaises(WithdrawalWeekendRestriccion):
            self.account.withdraw(200)
    
    def test_deposit_diferent_ammounts(self):
        test_cases = [
            {"ammount" : 500, "expected" : 1500},
            {"ammount" : 600, "expected" : 1600},
            {"ammount" : 1000, "expected" : 2000}
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
                self.assertEqual(self.account.deposit(case['ammount']), case["expected"])
    
    @unittest.skipUnless(BankAccount.is_api_available, "Api de cambio de moneda no disponible..")
    def test_api_available(self):
        self.assertEqual(self.account.money_conversion("COP", "USD",2000), 0.45066)
          
    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)
            
        if os.path.exists("other_account_log.txt"):
            os.remove("other_account_log.txt")