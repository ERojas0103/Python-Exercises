'''An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order.'''

widgets = int(input("numero de widgets: "))
gizmos = int(input("Numero de gizmos: "))

n_widgets = widgets * 75
n_gizmos = gizmos * 112

if n_widgets > 1000:

    n_widgets = n_widgets/1000
    print("Los Widgets pesan ", n_widgets, "kg")

else:

    print("Los Widgets pesan ", n_widgets, "g")

if n_gizmos > 1000:

    n_gizmos = n_gizmos/1000
    print("Los Widgets pesan ", n_gizmos, "kg")

else:

    print("Los Widgets pesan ", n_gizmos, "g")
