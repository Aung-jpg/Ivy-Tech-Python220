"""
Aung Aung
program that simulates an ATM (check bal, deposit, withdraw)
"""

balance = 100.0

while True:
    print("type the following letter to do the action:")
    while True:
        action = input("'b': check balance  'w': withdraw  'd': deposit  'q': quit\n")
        if action.lower() not in ['b', 'w', 'd', 'q']:
            print("that's not one of the actions")
            continue
        break

    if action.lower() == 'q':
        quit()

    if action.lower() == 'd':
        deposit = float(input("How much would you like to deposit: "))
        balance += deposit
        print(f"Your balance: {balance}")
    
    if action.lower() == 'w':
        withdraw = float(input("How much would you like to withdraw: "))
        balance -= withdraw
        print(f"Your balance: {balance}")

    if action.lower() == 'b':
        print(f"Your balance: {balance}")  
    print()
