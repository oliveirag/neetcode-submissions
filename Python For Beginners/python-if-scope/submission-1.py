def pay_bill(balance: int, bill: int) -> int:
    # if balance is greater than or equal to bill, return balance minus bill
    if balance >= bill:
        return balance - bill
    # otherwise return current balance
    return balance

# do not modify below this line
print(pay_bill(100, 50))
print(pay_bill(100, 100))
print(pay_bill(100, 150))
