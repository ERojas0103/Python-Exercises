#Calculate the area of a field in acres, 1 acre: 43.560

lenght = float(input("Please enter the lenght of your field: "))
width = float(input("Please enter the width of your field: "))

area = lenght * width
acrearea = area/43560

print("The area of your field in acres is : ", acrearea)