import json
import random
import threading
import time

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts  = {}
        self.next_account_number = 10000000

    def open_Account(self, customer_name, account_type, balance):
        if customer_name in self.customers:
            existing_customer = self.customers[customer_name]
        else:
            existing_customer = Customer(customer_name)
            self.customers[customer_name] = existing_customer

        account_number = self.next_account_number
        self.next_account_number += 1
        account = Account(account_number, account_type, balance)
        self.accounts[account_number] = account
        existing_customer.add_account(account)
        print(f"Account {account_number} ({account_type}) created for {customer_name} with balance ${balance}")
    
    def deposit_check(self, customer_name, account_id, deposit_amount):
        customer = self.check_customer(customer_name)
        account = self.check_account(customer, account_id)
        account.deposit(deposit_amount)
    
    def withdraw_check(self, customer_name, account_id, deposit_amount):
        customer = self.check_customer(customer_name)
        account = self.check_account(customer, account_id)
        account.withdraw(deposit_amount)

    def view_account(self, customer_name, account_id):
        customer = self.check_customer(customer_name)
        account = self.check_account(customer, account_id)
        account.view_balance()
    
    def check_customer(self, customer_name):
        if customer_name not in self.customers:
            print("Customer not found...")
            return
        customer = self.customers[customer_name]
        return customer
    
    def check_account(self, customer, account_id):
        account = next((acc for acc in customer.accounts if acc.account_number == account_id), None)
        if account is None:
            print("Account not found")
            return
        return account
    
    def start_interest_scheduler(self, interval=10):
        """Starts a background thread to apply interest every `interval` seconds"""
        def interest_loop():
            while True:
                for account in self.accounts.values():
                    account.add_interest()
                time.sleep(interval)

        thread = threading.Thread(target=interest_loop, daemon=True)
        thread.start()

class Account:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type =account_type
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def view_balance(self):
        print(f"\n Balance: {self.balance}")

    def add_interest(self, rate=0.10):
        """Adds interest if this is a Savings account"""
        if self.account_type.lower() == "savings":
            self.balance += self.balance * rate
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
