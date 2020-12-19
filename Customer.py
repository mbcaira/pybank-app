import PyBank
import Currencies

"""
User interface for interacting with the program.
"""

BANK = PyBank.PyBank.get_instance()
C = Currencies.Currencies.get_instance()


def setup_screen():
    in_setup = True
    while in_setup:
        print("ADD ACCOUNT")
        initial_accs = BANK.get_accounts()
        account_number = input("Please enter the account number: ")
        balance = input("Please enter the initial balance: ")
        BANK.create_account(account_number, balance)
        if initial_accs < BANK.get_accounts():
            print("Account successfully created.\n")
            in_setup = False


def deposit_screen():
    print("DEPOSIT SCREEN")
    account_number = input("Please enter the account number: ")
    amount = input("Please enter the amount you wish to deposit: ")
    currency = C.get_currency(input("Please select the currency you would "
                                    "like to make the deposit in:\n(1) CAD\n"
                                    "(2) USD\n(3) EUR\n"))
    BANK.deposit_funds(account_number, amount, currency)


def withdraw_screen():
    print("WITHDRAW SCREEN")
    account_number = input("Please enter the account number: ")
    amount = input("Please enter the amount you wish to withdraw: ")
    currency = C.get_currency(input("Please select the currency you would "
                                    "like to make the deposit in:\n(1) CAD\n"
                                    "(2) USD\n(3) EUR\n"))
    BANK.withdraw_funds(account_number, amount, currency)


def transfer_screen():
    print("TRANSFER SCREEN")
    outgoing_acc_num = input("Please enter the account number to transfer funds from: ")
    incoming_acc_num = input("Please enter the account number to transfer funds to: ")
    amount = input("Please enter the amount you wish to transfer: ")
    BANK.transfer_funds(incoming_acc_num, outgoing_acc_num, amount)


def show_balance():
    print("BALANCE SCREEN")
    account_number = input("Please enter the account number you wish to see the balance of: ")
    bal = BANK.get_balance(account_number)
    bal_str = "CA${:,.2f}".format(bal)
    print(f"Balance of account {account_number}: {bal_str}")


if __name__ == '__main__':
    """
    The user interface is launched here, taking users through the setup process and then displaying other options to
    the user.
    """
    print("Welcome to Ace Bank!")
    in_loop = True
    in_setup = True
    while in_setup:
        print("SETUP SCREEN")
        input("Please enter the customer ID: ")
        initial_accs = BANK.get_accounts()
        account_number = input("Please enter the account number: ")
        balance = input("Please enter the initial balance: ")
        BANK.create_account(account_number, balance)
        if initial_accs < BANK.get_accounts():
            print("Account successfully created.\n")
            in_setup = False

    while in_loop:
        print("\nACCOUNT MENU OPTIONS")
        print("(1) Setup another account\n(2) Deposit\n(3) Withdraw\n(4) Transfer balances\n"
              + "(5) Show balance\n(6) Exit\n")
        choice = input("Please type your selection.\n(Valid inputs are from 1-6): ")
        print("\n")
        if choice == "6":
            in_loop = False
            print("Thank you for using Ace Bank!\nHave a nice day!\n")
        elif choice == "1":
            setup_screen()
        elif choice == "2":
            deposit_screen()
        elif choice == "3":
            withdraw_screen()
        elif choice == "4":
            transfer_screen()
        elif choice == "5":
            show_balance()
        else:
            print("Invalid selection! Please enter a selection from 1-5.\n")
