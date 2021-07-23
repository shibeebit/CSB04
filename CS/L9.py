from random import randint

def new_account():
    account = {}
    account["name"] = input("name: ")
    account["address"] = input("address: ")
    account["phone"] = input("phone: ")
    account["amount"] = int(input("amount: "))
    pw = str(input("password: "))
    retype_pass = str(input("retype password: "))
    while retype_pass != pw:
        print("They don't match. Enter again please")
        pw = str(input("password: "))
        retype_pass = str((input("retype password: ")))
    account["password"] = pw
    account['account_number'] = randint(0, 1000000)
    return account

def display_account(account):
    print('name: ', account["name"])
    print('address: ', account["address"])
    print('phone: ', account["phone"])
    print('amount: ', account["amount"])
    print('account number: ', account["account_number"])


def change_pass(account):
    password = input("New password: ")
    retype_pass = input("Retype new password: ")
    while retype_pass != password:
        print("They don't match. Enter again please")
        password = input("password: ")
        retype_pass = (input("retype password: "))
    account["password"] = password


def deposit(account):
    deposit_amount = int(input("Deposit amount: "))
    account["amount"] += deposit_amount


def withdraw(account):
    withdraw_amount = int(input("Withdraw amount: "))
    while account["amount"] < withdraw_amount:
        print("You don't have enough money")
        withdraw_amount = int(input("Withdraw amount: "))
    account["amount"] += withdraw_amount

def login(accounts):
    acc_num = int(input("Enter your account number: "))
    acc_pw = str(input("Enter password: "))
    acc_nums = []
    for account in accounts:
        acc_nums.append(account['account_number'])
    for account in accounts:
        if acc_num not in acc_nums:
            print('Invalid account number')
            login(accounts)
        elif acc_num == account["account_number"] and acc_pw == account["password"]:
            print("You are logged in!")
            return account
            break
        else:
            print("Wrong password!")
            login(accounts)

def main2(account, accounts):
    print('\nSelect your operations from the menu \n1.Change password \n2.Deposit \n3.Withdraw \n4.Print \n5.Exit \n')
    choice3 = str(input('Your selection: '))
    if choice3 == "1":
        print('Your choice: 1')
        change_pass(account)
        print('Your password has been changed successfully.')
        main2(account, accounts)
    elif choice3 == "2":
        print('Your choice: 2')
        deposit(account)
        print('Operation successful')
        main2(account, accounts)
    elif choice3 == "3":
        print('Your choice: 3')
        withdraw(account)
        print('Operation successful')
        main2(account, accounts)
    elif choice3 == "4":
        print('Your choice: 4')
        display_account(account)
        print('Operation successful')
        main2(account, accounts)
    elif choice3 == "5":
        print('Your choice: 5')
        main1(accounts)

accounts = []

def main1(accounts):
    print('\nWelcome to our bank \n1.New account \n2.Operations \n3.Exit \n')
    choice = str(input("Your selection: "))
    if choice == "3":
        print("Bye!")
    elif choice == "1":
        print('Your choice: 1')
        account = new_account()
        accounts.append(account)
        print('\nCreate new account successfully:\n')
        display_account(account)
        choice2 = str(input(("\nPress 0 for main menu\nType 1 to quit")))
        if choice2 == "0":
            main1(accounts)
        elif choice2 == "1":
            print("Bye")
    elif choice == "2":
        print('Your choice: 2')
        account = login(accounts)
        main2(account, accounts)
    else:
        print('Wrong number!')
        main1(accounts)

main1(accounts)

        









