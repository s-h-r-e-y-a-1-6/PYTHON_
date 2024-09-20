def triangle(angle1, angle2, angle3):
    # Sum of angles must be 180 degrees, and each angle should be greater than 0
    if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
        return True
    else:
        return False

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Checking if the angles form a valid triangle
if triangle(angle1, angle2, angle3):
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.")
