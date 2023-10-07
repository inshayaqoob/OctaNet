import random
import datetime

class ATM:
    def __init__(self):
        self.users = {}  # Dictionary to store user data (user_id: [pin, balance, transaction_history])

    def create_account(self):
        user_id = input("Enter your User ID: ")
        pin = input("Create your PIN: ")
        self.users[user_id] = [pin, 0, []]  # Initialize user account with zero balance and empty transaction history
        print("Account created successfully.")
        user_id = self.authenticate()  # Authenticate the user after creating the account
        if user_id:
            self.main_interface(user_id)

    def authenticate(self):
        user_id = input("Enter your User ID: ")
        pin = input("Enter your PIN: ")
        if user_id in self.users and self.users[user_id][0] == pin:
            return user_id
        else:
            print("Authentication failed. Invalid User ID or PIN.")
            return None

    def display_options(self):
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Exit")

    def perform_transaction(self, user_id, option):
        if option == 1:  # Check Balance
            print(f"Your current balance: ${self.users[user_id][1]}")
        elif option == 2:  # Withdraw
            amount = int(input("Enter withdrawal amount: $"))
            if amount > 0 and amount <= self.users[user_id][1]:
                self.users[user_id][1] -= amount
                self.users[user_id][2].append((datetime.datetime.now(), "Withdrawal", amount))
                print(f"Withdrawal successful. Remaining balance: ${self.users[user_id][1]}")
            else:
                print("Invalid amount or insufficient funds.")
        elif option == 3:  # Deposit
            amount = int(input("Enter deposit amount: $"))
            if amount > 0:
                self.users[user_id][1] += amount
                self.users[user_id][2].append((datetime.datetime.now(), "Deposit", amount))
                print(f"Deposit successful. Updated balance: ${self.users[user_id][1]}")
            else:
                print("Invalid amount for deposit.")
        # Implement other transaction options (Transfer, Transaction History) here

    def main_interface(self, user_id):
        while True:
            print("ATM INTERFACE")
            self.display_options()
            option = int(input("Enter your choice: "))
            if option == 6:
                print("Exiting ATM. Goodbye!")
                break
            self.perform_transaction(user_id, option)

    def run(self):
        while True:
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.create_account()
            elif choice == 2:
                user_id = self.authenticate()
                if user_id:
                    self.main_interface(user_id)
            elif choice == 3:
                print("Exiting ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
