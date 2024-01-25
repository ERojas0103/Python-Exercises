'''In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.'''

Bottle_quantity = int(input("Input the amount of bottles of a liter or less: "))
Bottle_quantity2 = int(input("Input the amount of bottles of more than a liter: "))

refund_less = Bottle_quantity * 0.10
refund_more = Bottle_quantity2 * 0.25

total_refund = refund_more + refund_less

print("The amount of money you will be refunded is: ", total_refund, "$")