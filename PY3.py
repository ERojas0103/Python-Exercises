'''Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.'''

savings = float(input("Inserta el numero: "))
savings = round(savings, 2)


years = int(input("Cuantos años lo va a dejar: "))
i = 0
for i in range(years+1):

    print("Su total del año ", i, "Es ", savings, "$")
    interest = savings * 0.04
    savings = savings+interest
    savings = round(savings, 2)
    i = i+1
