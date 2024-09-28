class BankAccount:
    """Base class for all bank accounts."""

    def __init__(self, account_number, account_holder_name, balance=0, account_type="General"):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_type = account_type
        self.transaction_history = []

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")
        print(f"{amount} withdrawn. New balance: {self.balance}")

    def check_balance(self):
        """Check the current balance of the account."""
        print(f"Current balance: {self.balance}")

    def show_transaction_history(self):
        """Display transaction history."""
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


class SavingsAccount(BankAccount):
    """Class representing a savings account."""

    def __init__(self, account_number, account_holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder_name, balance, account_type="Savings")
        self.interest_rate = interest_rate

    def add_interest(self):
        """Add interest to the balance."""
        interest = self.balance * self.interest_rate
        self.deposit(interest)  # Use deposit method to update transaction history
        print(f"Interest added: {interest}")


class CurrentAccount(BankAccount):
    """Class representing a current account with overdraft protection."""

    def __init__(self, account_number, account_holder_name, balance=0, overdraft_limit=0):
        super().__init__(account_number, account_holder_name, balance, account_type="Current")
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Withdraw money from the account with overdraft protection."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self.balance + self.overdraft_limit:
            print("Insufficient balance and overdraft limit!")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")
        print(f"{amount} withdrawn. New balance: {self.balance} (Including overdraft)")


# Example usage
if __name__ == "__main__":
    accounts = {}

    while True:
        print("\nBank Account System:")
        print("1. Create Savings Account")
        print("2. Create Current Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Show Transaction History")
        print("7. Exit")

        choice = input("Choose an operation (1-7): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate (as decimal, e.g., 0.05 for 5%): "))
            accounts[account_number] = SavingsAccount(account_number, account_holder_name, initial_balance, interest_rate)
            print("Savings account created successfully.")

        elif choice == "2":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            accounts[account_number] = CurrentAccount(account_number, account_holder_name, initial_balance, overdraft_limit)
            print("Current account created successfully.")

        elif choice == "3":
            account_number = input("Enter account number to deposit: ")
            amount = float(input("Enter amount to deposit: "))
            if account_number in accounts:
                accounts[account_number].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            account_number = input("Enter account number to withdraw: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_number in accounts:
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "5":
            account_number = input("Enter account number to check balance: ")
            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found!")

        elif choice == "6":
            account_number = input("Enter account number to show transaction history: ")
            if account_number in accounts:
                accounts[account_number].show_transaction_history()
            else:
                print("Account not found!")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please choose again.")
