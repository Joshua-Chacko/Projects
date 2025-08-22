from bank import Bank
import time

def main() -> None:
    bank = Bank()
    bank.start_interest_scheduler(interval=10)

    while True:
        print("\n--- Bank Menu ---")
        print("1. Open Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")
        print("-----------------\n")
        
        choice = input("Enter Choice: ")
        if choice == '1':
            customer_name = input("Enter Customer Name: ")
            account_type = input("Enter Account Type (Checkings/Savings): ")
            initial_balance = int(input("Enter Initial Balance: "))
            bank.open_Account(customer_name, account_type, initial_balance)            
        elif choice == '2':
            customer_name = input("Enter Customer Name: ")
            account_id = int(input("Enter Account ID: "))
            deposit_amount = int(input("Enter Amount to Deposit: "))
            bank.deposit_check(customer_name, account_id, deposit_amount)
        elif choice == '3':
            customer_name = input("Enter Customer Name: ")
            account_id = int(input("Enter Account ID: "))
            deposit_amount = int(input("Enter Amount to Deposit: "))
            bank.withdraw_check(customer_name, account_id, deposit_amount)
        elif choice == '4':
            customer_name = input("Enter Customer Name: ")
            account_id = int(input("Enter Account ID: "))
            bank.view_account(customer_name, account_id)
        elif choice.lower() == 'exit':
            print("Exiting Bank...")
            time.sleep(1)
            break
        else:
            print("\nPlease Enter Valid Option...")
            time.sleep(1)
            


if __name__ == "__main__":
    main()