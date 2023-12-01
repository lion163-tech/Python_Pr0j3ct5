deposit = int(input('How much you wanna deposit?'))
balance = 0
def Bank_Account(balance):
    while balance > 0:
        return deposit + balance
    if deposit >= 999:
        return "You Are A Liar"
def Withdraw(amount):
    if amount > balance:
        print("ERROR! INSUFFICIENT FUNDS, YOU ARE BROKE")
    else:
        return balance - amount

print(Bank_Account(0))
        