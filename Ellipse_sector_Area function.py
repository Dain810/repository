import math

print("We define the ellipse sector between two points (x_1, y_1) and (x_2, y_2) on the ellipse as the area that is swept out from the origin to the ellipse.")
print("This is the function that finds the area of the given ellipse sector.")

components = input("semi_Major_axis, semi_minor_axis, x_1, y_1, x_2, y_2")
com_spl = components.split(", ")
semi_Major_axis = float(com_spl[0])
semi_minor_axis = float(com_spl[1])
x_1 = float(com_spl[2])
y_1 = float(com_spl[3])
x_2 = float(com_spl[4])
y_2 = float(com_spl[5])

def ellipse_sector_area(a, b, c, d):
    Area = (d - c) * a * b / 2
    return Area

if y_1>=0:
    theta_1 = math.acos(x_1/semi_Major_axis)
else:
    theta_1 = 2*math.pi-math.acos(x_1/semi_Major_axis)
    
if y_2>=0:
    theta_2 = math.acos(x_2/semi_Major_axis)
else:
    theta_2 = 2*math.pi-math.acos(x_2/semi_Major_axis)
    
if theta_1<theta_2:
    theta_tilde_1 = theta_1
else:
    theta_tilde_1 = theta_1 - 2*math.pi
    
if semi_Major_axis <= 0 or semi_minor_axis <= 0:
    print("Check that all semi-axises are positive!")
else:
    Ver_1 = (x_1)**2/(semi_Major_axis)**2 + (y_1)**2/(semi_minor_axis)**2
    Ver_2 = (x_2)**2/(semi_Major_axis)**2 + (y_2)**2/(semi_minor_axis)**2
    if round(Ver_1) != 1 or round(Ver_2) != 1:
        print("Check that all points are on the ellipse!")
    else:
        print("theta_1 =", theta_1)
        print("theta_2 =", theta_2)
        print("Area =", ellipse_sector_area(semi_Major_axis, semi_minor_axis, theta_tilde_1, theta_2))