import requests
import os
# from dotenv import load_dotenv
from datetime import datetime
from src.exceptions import InsuficientFoundError, WithdrawalTimeRestrictionError, WithdrawalWeekendRestriccion

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        # load_dotenv()
        self.balance = balance
        self.log_file = log_file
        self._log_transaccion("Cuenta creada")
        self.api_key = "88a7d9a458c62c189d481541"
        self.url_base = "https://v6.exchangerate-api.com/v6/"
        
    def _log_transaccion(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaccion(f"Deposited : {amount}. New Balance {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        today = datetime.now()
        
        if today.weekday() > 4:
            raise WithdrawalWeekendRestriccion(
                "Withdrawals are not allowed in thw weekends.."
            )
        
        if today.hour < 8 or today.hour > 17:
            raise WithdrawalTimeRestrictionError(
                "Withdrawals are only allowed from 8am to 5pm.."
            )  
        
        if amount > self.balance:
            raise InsuficientFoundError(
                "The amount to retire exceeds de current balence."
            )    
        if amount > 0:
            self.balance -= amount
            self._log_transaccion(f"Retired : {amount}. New Balance {self.balance}")
        return self.balance
    
    def transfer(self, mount_to_trasnfer, account_to_transfer):
        if mount_to_trasnfer > 0 and mount_to_trasnfer <= self.balance:
            self.balance -= mount_to_trasnfer
            account_to_transfer.deposit(mount_to_trasnfer)
            self._log_transaccion(f"Success transfer : {mount_to_trasnfer} to account {account_to_transfer}. New Balance {self.balance}")
            return self.balance
        else:
            self._log_transaccion(f"Error transfer : {mount_to_trasnfer} to account {account_to_transfer}.")
            raise ValueError(f"Error : You can not transfer {mount_to_trasnfer}, because there is not enogh money...")
            
    def get_balance(self):
        self._log_transaccion(f"Current Balance : {self.balance}")
        return  self.balance    
    
    def is_api_available(self):
        url = f"{self.url_base}{self.api_key}/latest/COP"
        response = requests.get(url)
        return True if response.status_code == 200 else False
    
    def money_conversion(self, money_from, money_to, mount):
        url = f"{self.url_base}{self.api_key}/pair/{money_from}/{money_to}/{mount}"
        response = requests.get(url)
        return response.json()['conversion_result']
    
    