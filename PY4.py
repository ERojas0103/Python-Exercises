'''Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 '''
import math

a = int(input("Integer one: "))
b = int(input("Integer two: "))

sum = a+b
print(sum)

subs = a-b
print(subs)

pro = a*b
print(pro)

quo = a/b
print(quo)

rem = a % b
print(rem)

log = math.log(10)
print(log)
