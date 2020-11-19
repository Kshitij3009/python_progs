print('''1. Area of circle
2. Area of rectangle
3. Area of square 
4. Circumference of circle
''')
a = int(input("Choose what you have to find: "))
print("")
if a == 1:
    r = float(input("enter radius: "))
    print("area of circle = ", 3.14 * r**2)
elif a == 2:
    L = float(input("Enter the length of rectangle: "))
    B = float(input("Enter breadth of the rectangle: "))
    print("area of rectangle = ", L*B)
elif a == 3:
    s = float(input("Enter the side of square: "))
    print("area of square = ", s**2)
elif a == 4:
    r = float(input("Enter the radius of circle: "))
    print("circumference of circle =", 2*3.14*r)
else:
    print("Enter a valid option")
