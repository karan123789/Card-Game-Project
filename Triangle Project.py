import math
BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''

print(BANNER)
count = 0
# a counter to determne # of valid triangles throughout the program
print()
PROMPT = "Do you wish to process a triangle (Y or N)?  "
# asks the user wheter they wanto input a triangle sides or not
promptmenu_str = input(PROMPT)
if promptmenu_str == "N" or promptmenu_str == "n":
    print("\nNumber of valid triangles:", count)
    # if they type N or n then the program ends
    quit()


while promptmenu_str == "Y" or promptmenu_str == "y":
    # when users input Y or y plays the following program
    ab_str = input('\nEnter length of side AB: ')
    c = int(ab_str)  # converts str into int
    bc_str = input('\nEnter length of side BC: ')
    a = int(bc_str)  # converts str into int
    ca_str = input('\nEnter length of side CA: ')
    b = int(ca_str)  # converts str into int
    if c + a == b:
        # if the first two sides equal the last big side then it is a deg. triangle
        print("\n\n  Degenerate Triangle")
        PROMPT = "\nDo you wish to process another triangle? (Y or N) "
        promptmenu_str = input(PROMPT)
        if promptmenu_str == "N" or promptmenu_str == "n":
            print("\nNumber of valid triangles:", count)
            quit()
    elif c + a < b:
        # if the two sides are less than the lat one then it is not a triangle
        print("\n\n  Not a Triangle")
        PROMPT = "\nDo you wish to process another triangle? (Y or N) "
        promptmenu_str = input(PROMPT)
        if promptmenu_str == "N" or promptmenu_str == "n":
            print("\nNumber of valid triangles:", count)
            quit()
    elif c + a > b or a + b > c:
        # if the two isdes are greater than the last oen then it is a triangle
        print("\n\n  Valid Triangle")
        count += 1
        anglea = math.degrees(math.acos((((b**2)+(c**2)-(a**2))/(2.0*b*c))))
        # calcs the interior angle for A using law of cosines
        angleb = math.degrees(math.acos((((a**2)+(c**2)-(b**2))/(2.0*a*c))))
        # calcs the interior angle for B using law of cosines
        anglec = math.degrees(math.acos((((a**2)+(b**2)-(c**2))/(2.0*a*b))))
        # calcs the interior angle for C using law of cosines
        randa = round(math.radians(anglea), 1)
        # converts the anglea degrees into radians and rounds it
        randb = round(math.radians(angleb), 1)
        # converts the angleb degrees into radians and roudnds it
        randc = round(math.radians(anglec), 1)
        # converts the anglec degrees into radians and rounds it
        s = (a+b+c)/2
        # the s value when calc the area using heron's formula
        perimeter = float(a + b + c)
        # formula to calc perimneter of the triangle with three sides
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        # calcs the area using heron's formula
        print("\n  Triangle sides:")
        print("    Length of side AB:", float(c))
        print("    Length of side BC:", float(a))
        print("    Length of side CA:", float(b))
        # types out the three sides inputted by the user
        print("\n  Degree measure of interior angles:")
        print("    Angle A:", round(anglea, 1))
        print("    Angle B:", round(angleb, 1))
        print("    Angle C:", round(anglec, 1))
        # takes the interior angle measures from law of cosines and types it out
        print("\n  Radian measure of interior angles:")
        print("    Angle A:", randa)
        print("    Angle B:", randb)
        print("    Angle C:", randc)
        # takes the degrees converted to radians and types it out
        print("\n  Perimeter and Area of triangle:")
        print("    Perimeter of triangle:", perimeter)
        print("    Area of triangle:", round(area, 1))
        # types out the perineter and area calculated form the three sides
        print("\n  Types of triangle:")
        if a == b and angleb != 90:
            # if one side equal to another and one angle not equal to 90 then it
            # is the following triangles
            print("    Isosceles Triangle")
            print("    Equilateral Triangle")
            print("    Oblique Triangle")
        elif c != a and anglea != 90 and angleb > 90:
            # if one side doesnt equal other and one angle doenst equal 90 and one less
            # than 90 then it is going to print out the following triangles
            print("    Scalene Triangle")
            print("    Oblique Triangle")
            print("    Obtuse Triangle")
        elif a == b != c or b == c != a or c == a != b and anglea != 90:
            # if the follwoign conditions are met from the sides inputted prints out the
            # following types of triangles
            print("    Isosceles Triangle")
            print("    Oblique Triangle")
        elif a != b != c and angleb == 90:
            # if none of the sides equal each other and one angle is equal to 90 prints
            # out the following types of triangles
            print("    Scalene Triangle")
            print("    Right Triangle")
        PROMPT = "\nDo you wish to process another triangle? (Y or N) "
        # asks the user at the end of the program if they want to play again and keeps
        # a counter of valid triangles being inputted
        promptmenu_str = input(PROMPT)
        if promptmenu_str == "N" or promptmenu_str == "n":
            print("\nNumber of valid triangles:", count)
