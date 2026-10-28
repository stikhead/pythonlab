class BankAccount:
    """
    Base class representing a generic bank account with encapsulated private attributes.
    """
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = initial_balance

    def get_balance(self) -> float:
        return self.__balance
    
    def _set_balance(self, amount: float):
        self.__balance = amount

    def get_account_details(self) -> str:
        return f"Account: {self.__account_number} | Holder: {self.__holder_name}"

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New Balance: ${self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> bool:
        """Base withdrawal logic: strictly prevents overdrafts."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}. New Balance: ${self.__balance:.2f}")
            return True
        else:
            print("Withdrawal failed: Insufficient funds or invalid amount.")
            return False

    def display_info(self):
        """Displays account summary."""
        print(f"{self.get_account_details()} | Balance: ${self.__balance:.2f}")


class SavingsAccount(BankAccount):
    """
    Derived class representing a savings account with transaction fees and interest.
    """
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0, interest_rate: float = 0.03):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate
        self.withdrawal_fee = 2.00

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        super().deposit(interest)
        print(f"Interest of ${interest:.2f} applied.")

    def withdraw(self, amount: float) -> bool:
        """
        Method overriding for balance transactions via super().
        Applies a mandatory withdrawal fee on top of the requested amount.
        """
        print(f"Processing Savings withdrawal (includes ${self.withdrawal_fee:.2f} fee)...")
        return super().withdraw(amount + self.withdrawal_fee)

    def display_info(self):
        super().display_info()
        print(f"   -> [Type: Savings | Interest Rate: {self.interest_rate * 100}%]")


class CurrentAccount(BankAccount):
    """
    Derived class representing a current/checking account with an overdraft limit.
    """
    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> bool:
        """
        Method overriding to allow transactions within an overdraft limit.
        """
        print("Processing Current Account withdrawal...")
        current_balance = self.get_balance()
        if amount <= current_balance:
            return super().withdraw(amount)
        elif amount <= (current_balance + self.overdraft_limit):
            self._set_balance(current_balance - amount)
            print(f"Withdrew ${amount:.2f} (Overdraft utilized). New Balance: ${self.get_balance():.2f}")
            return True
        else:
            print("Withdrawal failed: Exceeds available balance and overdraft limit.")
            return False

    def display_info(self):
        super().display_info()
        print(f"   -> [Type: Current | Overdraft Limit: ${self.overdraft_limit:.2f}]")


def execute_daily_batch(accounts: list):
    """
    Polymorphic interface manager: Iterates through various account types
    and triggers their overridden methods identically.
    """
    print("\n--- Running Daily Batch Transactions ---")
    for account in accounts:
        print("-" * 40)
        account.display_info()
        account.withdraw(100.0)  # Acts differently based on account type
        
        if isinstance(account, SavingsAccount):
            account.apply_interest()


if __name__ == "__main__":
    base_acc = BankAccount("BA-001", "Alice Base", 200.0)
    save_acc = SavingsAccount("SA-102", "Bob Saver", 200.0, interest_rate=0.05)
    curr_acc = CurrentAccount("CA-203", "Charlie Current", 50.0, overdraft_limit=300.0)

    bank_database = [base_acc, save_acc, curr_acc]
    execute_daily_batch(bank_database)
    
    print("-" * 40)
    print("\n--- Final Account States ---")
    for acc in bank_database:
        acc.display_info()