'''
greetings = "Hello version {greetings:.2f}!"
print(greetings.format(greetings = 1))
#import random #import random for the random square option
import math #import math for finding the area of the circle shapes
import random #import random is for the random square
from math import pi
'''
#this checks for the password if its correct or not
def check_password():
    for i in range(3):
        pw = input("Enter password:")
        if pw.isalnum():
            if pw == "squareyay":
                print("Correct!")
                break
            else:
                print("Inputted password is incorrect. Please try again.")
        else:
            print("Password is not alphanum Please try again.")
        if i == 2:
            print("Maximum attempts exceeded.")
            exit()

(check_password())
print("Custom Shape can be made using these shape options are below!\n")
print("Shape options are Circle, Square, Triangle, Rhombus, Parallelogram, Arrow and a Kite!" "\n")
print("the top half can be added to all shapes" "\n")
print("the bottom half can be added to these shapes rhombus, arrow, kite"" \n")
art_mode = input("Activate infinite mode? y/n:") #determines if the infinite mode function will be used
print("Put random for random square! \n ")
shape_type = input("What is the shape: \n") #Determines what the shape type is
shape_key_type = input("What is the top half made of for the shape: " "\n") #Determines what the key the bottom and top of a no fill square will be made of. This is also the base of all fill in shapes
secondary_shape_key_type = input("what is the bottom half made of for the shape:" "\n") #Only is used for no fill square this determines the no fill square sides
shape_key_type_sides = secondary_shape_key_type 
Dict_keys = { #dictionary of all the keys on the Querty keyboard
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "!",
    11: "@",
    12: "#",
    13: "$",
    14: "%",
    15: "^",
    16: "&",
    17: "*",
    28: "(",
    29: "-",
    30: "w",
    31: "+",
    32: "~",
    33: "`",
    34: "/",
    35: "*",
    36: "-",
    37: "q",
    38: "w",
    39: "e",
    40: "r",
    41: "t",
    42: "y",
    43: "u",
    44: "i",
    45: "=",
    46: "o",
    47: "p",
    48: "[",
    49: "{",
    50: "]",
    51: "|",
    52: "Q",
    53: "W",
    54: "E",
    55: "R",
    56: "T",
    57: "Y",
    58: "U",
    59: "I",
    60: "O",
    61: "P",
    62: "a",
    63: "s",
    64: "d",
    65: "f",
    66: "g",
    67: "h",
    68: "j",
    69: "k",
    70: "l",
    71: ";",
    72: ":",
    73: "A",
    74: "S",
    75: "D",
    76: "F",
    77: "G",
    78: "H",
    79: "J",
    80: "K",
    81: "L",
    82: "z",
    83: "x",
    84: "c",
    85: "v",
    86: "b",
    87: "n",
    88: "m",
    89: ",",
    90: ".",
    91: "/",
    92: "Z",
    93: "X",
    94: "C",
    95: "V",
    96: "B",
    97: "N",
    98: "M",
    99: "<",
    100: ">",
    101: "?",
}
#this takes the key out of the dictionary and defines the key that is desired
if shape_key_type == "1":
    Key_desired = Dict_keys.get(1)
if shape_key_type == "2":
    Key_desired = Dict_keys.get(2)
if shape_key_type == "3":
    Key_desired = Dict_keys.get(3)
if shape_key_type == "4":
    Key_desired = Dict_keys.get(4)
if shape_key_type == "5":
    Key_desired = Dict_keys.get(5)
if shape_key_type == "6":
    Key_desired = Dict_keys.get(6)
if shape_key_type == "7":
    Key_desired = Dict_keys.get(7)
if shape_key_type == "8":
    Key_desired = Dict_keys.get(8)
if shape_key_type == "9":
    Key_desired = Dict_keys.get(9)
if shape_key_type == "!":
    Key_desired = Dict_keys.get(10)
if shape_key_type == "@":
    Key_desired = Dict_keys.get(11)
if shape_key_type == "#":
    Key_desired = Dict_keys.get(12)
if shape_key_type == "$":
    key_desired = Dict_keys.get(13)
if shape_key_type == "%":
    Key_desired = Dict_keys.get(14)
if shape_key_type == "^":
    Key_desired = Dict_keys.get(15)
if shape_key_type == "&":
    Key_desired = Dict_keys.get(16)
if shape_key_type == "*":
    Key_desired = Dict_keys.get(17)
if shape_key_type == "(":
    Key_desired = Dict_keys.get(28)
if shape_key_type == "-":
    Key_desired = Dict_keys.get(29)
if shape_key_type == "-":
    Key_desired = Dict_keys.get(30)
if shape_key_type == "w":
    Key_desired = Dict_keys.get(31)
if shape_key_type == "+":
    Key_desired = Dict_keys.get(32)
if shape_key_type == "`":
    Key_desired = Dict_keys.get(33)
if shape_key_type == "/":
    Key_desired = Dict_keys.get(34)
if shape_key_type == "*":
    Key_desired = Dict_keys.get(35)
if shape_key_type == "-":
    Key_desired = Dict_keys.get(36)
if shape_key_type == "q":
    Key_desired = Dict_keys.get(37)
if shape_key_type == "w":
    Key_desired = Dict_keys.get(38)
if shape_key_type == "e":
    Key_desired = Dict_keys.get(39)
if shape_key_type == "r":
    Key_desired = Dict_keys.get(40)
if shape_key_type == "t":
    Key_desired = Dict_keys.get(41)
if shape_key_type == "y":
    Key_desired = Dict_keys.get(42)
if shape_key_type == "u":
    Key_desired = Dict_keys.get(43)
if shape_key_type == "i":
    Key_desired = Dict_keys.get(44)
if shape_key_type == "=":
    Key_desired = Dict_keys.get(45)
if shape_key_type == "o":
    Key_desired = Dict_keys.get(46)
if shape_key_type == "p":
    Key_desired = Dict_keys.get(47)
if shape_key_type == "a":
    Key_desired = Dict_keys.get(48)
if shape_key_type == "[":
    Key_desired = Dict_keys.get(49)
if shape_key_type == "}":
    Key_desired = Dict_keys.get(50)
if shape_key_type == "|":
    Key_desired = Dict_keys.get(51)
if shape_key_type == "Q":
    Key_desired = Dict_keys.get(52)
if shape_key_type == "W":
    Key_desired = Dict_keys.get(53)
if shape_key_type == "E":
    Key_desired = Dict_keys.get(54)
if shape_key_type == "R":
    Key_desired = Dict_keys.get(55)
if shape_key_type == "T":
    Key_desired = Dict_keys.get(56)
if shape_key_type == "Y":
    Key_desired = Dict_keys.get(57)
if shape_key_type == "U":
    Key_desired = Dict_keys.get(58)
if shape_key_type == "I":
    Key_desired = Dict_keys.get(59)
if shape_key_type == "O":
    Key_desired = Dict_keys.get(60)
if shape_key_type == "P":
    Key_desired = Dict_keys.get(61)
if shape_key_type == "a":
    Key_desired = Dict_keys.get(62)
if shape_key_type == "s":
    Key_desired = Dict_keys.get(63)
if shape_key_type == "d":
    Key_desired = Dict_keys.get(64)
if shape_key_type == "f":
    Key_desired = Dict_keys.get(65)
if shape_key_type == "g":
    Key_desired = Dict_keys.get(66)
if shape_key_type == "h":
    Key_desired = Dict_keys.get(67)
if shape_key_type == "j":
    Key_desired = Dict_keys.get(68)
if shape_key_type == "k":
    Key_desired = Dict_keys.get(69)
if shape_key_type == "l":
    Key_desired = Dict_keys.get(70)
if shape_key_type == ";":
    Key_desired = Dict_keys.get(71)
if shape_key_type == ":":
    Key_desired = Dict_keys.get(72)
if shape_key_type == "A":
    Key_desired = Dict_keys.get(73)
if shape_key_type == "S":
    Key_desired = Dict_keys.get(74)
if shape_key_type == "D":
    Key_desired = Dict_keys.get(75)
if shape_key_type == "F":
    Key_desired = Dict_keys.get(76)
if shape_key_type == "G":
    Key_desired = Dict_keys.get(77)
if shape_key_type == "H":
    Key_desired = Dict_keys.get(78)
if shape_key_type == "J":
    Key_desired = Dict_keys.get(79)
if shape_key_type == "K":
    Key_desired = Dict_keys.get(80)
if shape_key_type == "L":
    Key_desired = Dict_keys.get(81)
if shape_key_type == "z":
    Key_desired = Dict_keys.get(82)
if shape_key_type == "x":
    Key_desired = Dict_keys.get(83)
if shape_key_type == "c":
    Key_desired = Dict_keys.get(84)
if shape_key_type == "v":
    Key_desired = Dict_keys.get(85)
if shape_key_type == "b":
    Key_desired = Dict_keys.get(86)
if shape_key_type == "n":
    Key_desired = Dict_keys.get(87)
if shape_key_type == "m":
    Key_desired = Dict_keys.get(88)
if shape_key_type == ",":
    Key_desired = Dict_keys.get(89)
if shape_key_type == ".":
    Key_desired = Dict_keys.get(90)
if shape_key_type == "/":
    Key_desired = Dict_keys.get(91)
if shape_key_type == "":
    Key_desired = Dict_keys.get(92)
if shape_key_type == "a":
    Key_desired = Dict_keys.get(93)
if shape_key_type == "[":
    Key_desired = Dict_keys.get(94)
if shape_key_type == "}":
    Key_desired = Dict_keys.get(95)
if shape_key_type == "|":
    Key_desired = Dict_keys.get(96)
if shape_key_type == "Q":
    Key_desired = Dict_keys.get(97)
if shape_key_type == "W":
    Key_desired = Dict_keys.get(98)
if shape_key_type == "E":
    Key_desired = Dict_keys.get(99)
if shape_key_type == "R":
    Key_desired = Dict_keys.get(100)
if shape_key_type == "u":
    Key_desired = Dict_keys.get(101)
#this one is for the no fill square sides and it defines what Key_side_desired is by taking it from the dictionary
if shape_key_type_sides == "1":
    Key_side_desired = Dict_keys.get(1)
if shape_key_type_sides == "2":
    Key_side_desired = Dict_keys.get(2)
if shape_key_type_sides == "3":
    Key_side_desired = Dict_keys.get(3)
if shape_key_type_sides == "4":
    Key_side_desired = Dict_keys.get(4)
if shape_key_type_sides == "5":   
    Key_side_desired = Dict_keys.get(5)
if shape_key_type_sides == "6":
    Key_side_desired = Dict_keys.get(6)
if shape_key_type_sides == "7":
    Key_side_desired = Dict_keys.get(7)
if shape_key_type_sides == "8":
    Key_side_desired = Dict_keys.get(8)
if shape_key_type_sides == "9":
    Key_side_desired = Dict_keys.get(9)
if shape_key_type_sides == "!":
    Key_side_desired = Dict_keys.get(10)
if shape_key_type_sides == "@":
    Key_side_desired = Dict_keys.get(11)
if shape_key_type_sides == "#":
    Key_side_desired = Dict_keys.get(12)
if shape_key_type_sides == "$":
    Key_side_desired = Dict_keys.get(13)
if shape_key_type_sides == "%":
    Key_side_desired = Dict_keys.get(14)
if shape_key_type_sides == "^":
    Key_side_desired = Dict_keys.get(15)
if shape_key_type_sides == "&":
    Key_side_desired = Dict_keys.get(16)
if shape_key_type_sides == "*":
    Key_side_desired = Dict_keys.get(17)
if shape_key_type_sides == "(":
    Key_side_desired = Dict_keys.get(28)
if shape_key_type_sides == "-":
    Key_side_desired = Dict_keys.get(29)
if shape_key_type_sides == "-":
    Key_side_desired = Dict_keys.get(30)
if shape_key_type_sides == "w":
    Key_side_desired = Dict_keys.get(31)
if shape_key_type_sides == "+":
    Key_side_desired = Dict_keys.get(32)
if shape_key_type_sides == "`":
    Key_side_desired = Dict_keys.get(33)
if shape_key_type_sides == "/":
    Key_side_desired = Dict_keys.get(34) 
if shape_key_type_sides == "*":
    Key_side_desired = Dict_keys.get(35)
if shape_key_type_sides == "-":
    Key_side_desired = Dict_keys.get(36)
if shape_key_type_sides == "q":
    Key_side_desired = Dict_keys.get(37) 
if shape_key_type_sides == "w":
    Key_side_desired = Dict_keys.get(38)
if shape_key_type_sides == "e":
    Key_side_desired = Dict_keys.get(39)
if shape_key_type_sides == "r":
    Key_side_desired = Dict_keys.get(40)
if shape_key_type_sides == "t":
    Key_side_desired = Dict_keys.get(41) 
if shape_key_type_sides == "y":
    Key_side_desired = Dict_keys.get(42)
if shape_key_type_sides == "u":
    Key_side_desired = Dict_keys.get(43)
if shape_key_type_sides == "i":
    Key_side_desired = Dict_keys.get(44)
if shape_key_type_sides == "=":
    Key_side_desired = Dict_keys.get(45) 
if shape_key_type_sides == "o":
    Key_side_desired = Dict_keys.get(46)
if shape_key_type_sides == "p":
    Key_side_desired = Dict_keys.get(47) 
if shape_key_type_sides == "a":
    Key_side_desired = Dict_keys.get(48)
if shape_key_type_sides == "[":
    Key_side_desired = Dict_keys.get(49)
if shape_key_type_sides == "}":
    Key_side_desired = Dict_keys.get(50)
if shape_key_type_sides == "|":
    Key_side_desired = Dict_keys.get(51) 
if shape_key_type_sides == "Q":
    Key_side_desired = Dict_keys.get(52)  
if shape_key_type_sides == "W":
    Key_side_desired = Dict_keys.get(53)
if shape_key_type_sides == "E":
    Key_side_desired = Dict_keys.get(54) 
if shape_key_type_sides == "R":
    Key_side_desired = Dict_keys.get(55)
if shape_key_type_sides == "T":
    Key_side_desired = Dict_keys.get(56)
if shape_key_type_sides == "Y":
    Key_side_desired = Dict_keys.get(57)
if shape_key_type_sides == "U":
    Key_side_desired = Dict_keys.get(58)
if shape_key_type_sides == "I":
    Key_side_desired = Dict_keys.get(59)
if shape_key_type_sides == "O":
    Key_side_desired = Dict_keys.get(60)
if shape_key_type_sides == "P":
    Key_side_desired = Dict_keys.get(61)
if shape_key_type_sides == "a":
    Key_side_desired = Dict_keys.get(62)
if shape_key_type_sides == "s":
    Key_side_desired = Dict_keys.get(63) 
if shape_key_type_sides == "d":
    Key_side_desired = Dict_keys.get(64)
if shape_key_type_sides == "f":
    Key_side_desired = Dict_keys.get(65) 
if shape_key_type_sides == "g":
    Key_side_desired = Dict_keys.get(66)
if shape_key_type_sides == "h":
    Key_side_desired = Dict_keys.get(67)
if shape_key_type_sides == "j":
    Key_side_desired = Dict_keys.get(68)
if shape_key_type_sides == "k":
    Key_side_desired = Dict_keys.get(69) 
if shape_key_type_sides == "l":
    Key_side_desired = Dict_keys.get(70)  
if shape_key_type_sides == ";":
    Key_side_desired = Dict_keys.get(71)
if shape_key_type_sides == ":":
    Key_side_desired = Dict_keys.get(72) 
if shape_key_type_sides == "A":
    Key_side_desired = Dict_keys.get(73)
if shape_key_type_sides == "S":
    Key_side_desired = Dict_keys.get(74)
if shape_key_type_sides == "D":
    Key_side_desired = Dict_keys.get(75)
if shape_key_type_sides == "F":
    Key_side_desired = Dict_keys.get(76)
if shape_key_type_sides == "G":
    Key_side_desired = Dict_keys.get(77)
if shape_key_type_sides == "H":
    Key_side_desired = Dict_keys.get(78)
if shape_key_type_sides == "J":
    Key_side_desired = Dict_keys.get(79)  
if shape_key_type_sides == "K":
    Key_side_desired = Dict_keys.get(80)
if shape_key_type_sides == "L":
    Key_side_desired = Dict_keys.get(81) 
if shape_key_type_sides == "z":
    Key_side_desired = Dict_keys.get(82)
if shape_key_type_sides == "x":
    Key_side_desired = Dict_keys.get(83)
if shape_key_type_sides == "c":
    Key_side_desired = Dict_keys.get(84)
if shape_key_type_sides == "v":
    Key_side_desired = Dict_keys.get(85)
if shape_key_type_sides == "b":
    Key_side_desired = Dict_keys.get(86)
if shape_key_type_sides == "n":
    Key_side_desired = Dict_keys.get(87)
if shape_key_type_sides == "m":
    Key_side_desired = Dict_keys.get(88)
if shape_key_type_sides == ",":
    Key_side_desired = Dict_keys.get(89)
if shape_key_type_sides == ".":
    Key_side_desired = Dict_keys.get(90) 
if shape_key_type_sides == "/":
    Key_side_desired = Dict_keys.get(91)
if shape_key_type_sides == "":
    Key_side_desired = Dict_keys.get(92) 
if shape_key_type_sides == "a":
    Key_side_desired = Dict_keys.get(93)
if shape_key_type_sides == "[":
    Key_side_desired = Dict_keys.get(94)
if shape_key_type_sides == "}":
    Key_side_desired = Dict_keys.get(95)
if shape_key_type_sides == "|":
    Key_side_desired = Dict_keys.get(96) 
if shape_key_type_sides == "Q":
    Key_side_desired = Dict_keys.get(97)  
if shape_key_type_sides == "W":
    Key_side_desired = Dict_keys.get(98)
if shape_key_type_sides == "E":
    Key_side_desired = Dict_keys.get(99) 
if shape_key_type_sides == "R":
    Key_side_desired = Dict_keys.get(100)
if shape_key_type_sides == "u":
    Key_side_desired = Dict_keys.get(101)
'''
the draw_circle function is used to create a circle it does this by taking in the radius which is the circumference divided by 2
then it takes the sides aka the height of the circle  and uses it with the lenth to create the outer shell of the circle
next the distance variable is used to fill in the inside of the circle as the distance becomes smaller then the radius then it will not expand out of the radius
'''
def draw_circle(radius): #this function is used to create the circle 
    for sides in range(-radius, radius+1): #this is for the middle of the height for the circle this is like the starting point for how tall the circle will be the Plus 1 is needed because without it the sides of the circle will be uneven.
        for lenth in range(-radius, radius+1): #this is for the width of the middle part of the circle this is like the starting point for how wide the circle will.
            distance = math.sqrt(lenth**2 + sides**2) 
            if distance <= radius:
                print(Key_desired, end=" ")
            else:
                print(" ", end=" ")
        print()
if shape_type == "circle":
    diameter =  int (input("what is the diameter of the circle:"))
    radius = diameter //  2 #to turn the circumference into radius by dividing by 2
    (draw_circle(radius))
    area_circle = pi * radius**2
    area_circle_rounded = round(area_circle, 3)
    print("the area of the circle is", area_circle_rounded)
'''
the shape_function_design function 
this function the bulk of processing the shape that was entered and the key that the shape will be made of
it also holds sub shapes which are a shape type under a primary shape type these are  Circle, Square, Triangle, Rhombus, Parallelogram, Pentagon, Arrow and Kite.
the Triangle and Square has sub shape types which are the Obtuse Triangle, Right Triangle, Isoceles square, No fill square and fill square.
basically what this function does is it takes in the shape_type variable, then the function goes through each of it's if statements until it detects what shape was entered with text.
after that if a shape has a sub shape some more input questions will be asked to fit the criteria needs of the sub shape.
then the shape_type is returned with the shape width, height, and the keys desired and will be ready to print.
next the function is called and the shape is printed.
The function returns shape_type whihch is what ever the shape is will be printed 
'''
def shape_fuction_design(shape_type):
    if shape_type == "square":  #checks if shape is square
        height = input("Height of Shape?" "\n")
        width = input("Width of Shape?" "\n")
        width = int(width)
        height = int(height)
        square_type = input("Square options are fill or nofill:") 
        if square_type == "fill": #checks if shape type is fill
            for s in range(height):
                print(str(Key_desired  * width))
            char_total = height * width
            print("Total key amount in square is:", char_total)
            print("Filled Square with Key Desired!")
        if square_type == "nofill": #checks if the squrae is nofill
            width = int(width)
            height = int(height)
            print(str(Key_desired) * width)
            for _ in range(height - 2):
                print(str(Key_side_desired) + " " * (width - 2) + str(Key_side_desired))
            print(str(Key_desired) * width)
            char_total = (width + height - 2) * 2
            print("nofill Square with Keys Desired!")
            print("toatl key amount is:", char_total)  
        return shape_type
        
    if shape_type == "random"  and "r": #checks if shape type is random 
        
            height_random = random.randint(1,55)
            width_random = random.randint(1, 60)
            height = height_random
            width = width_random
        
            print(str(Key_desired * width))
            for e in range(height):
                    print(str(Key_side_desired) + " " * (height) + str(Key_side_desired))
            print(str(Key_desired) * (width))
            return shape_type
    if shape_type == "triangle":
        print("Triangle options are: Right, Obtuse, Isoceles and Equilateral! \n")
        triangle_type = input("What type of triangle:")
        bottom_leg = int (input("what is the lenth of the bottom part of the triangle:"))
        if triangle_type == "obtuse":
            for t in range(bottom_leg):
                print(" " * (bottom_leg + t - 1) + (str(Key_desired)) * (t + 1))
            shape_type = "obtuse Triangle"
            print("Obtuse triangle!")
            return shape_type
        right = 1
        if triangle_type == "right": #checks if triangle type is right
            for t in range((int(bottom_leg) + (int(right)))):
                print(Key_desired * t)
            area = bottom_leg**2 / 2
            shape_type = "right triangle"
            print("Right triangle area is:", area)
            return shape_type
        if triangle_type == "equilateral": #checks if triangle is equilateral
            for i in range(bottom_leg):
                print(" " * (bottom_leg - i - 1) + ((str(Key_desired + " "))) * (i + 1))
            shape_type = "equilateral triangle"
            area = (math.sqrt(3) / 4) * bottom_leg ** 2
            area_rounded = round(area, 3)
            print("equilateral Triangle area is", area_rounded)
            return shape_type
        if triangle_type == "isoceles":
            for i in range(bottom_leg):
                spaces = ' ' * (bottom_leg - i - 1)
                keys_part = Key_desired * (2 * i + 1)
                print(spaces + keys_part + spaces)
                area = (1/2) * bottom_leg * bottom_leg
            print("Isoceles triangle area is", area)
            return shape_type

    if shape_type == "parallelogram": #checks if shape type is parallelogram
        while True:
            par_lenth = input("how long is the top and bottom of the Parallelogram:")
            par_lenth = int(par_lenth)
            for i in range(par_lenth):
                print(" " * (par_lenth - i - 1) + (str(Key_desired) * (par_lenth)))
            print("Parallelogram!")
            return shape_type
            break
    if shape_type == "arrow": #checks if shape type is arrow
        while True:
            mid_arrow = input("How long is the  middle of the Arrow:")
            mid_arrow = int(mid_arrow)
            for r in range(mid_arrow):
                print(" " * (mid_arrow - r - 1) + ((str(Key_desired + " " ))) * (r + 1))
            for e in range(mid_arrow - 1):
                print(" " * (mid_arrow - e - 1) + ((str(Key_side_desired + " "))) * (e + 1))
            print("arrow!")
            return shape_type
    if shape_type == "rhombus": #checks if shape type is rhombus
        print("rhombus types are diamond, regular, and right!")
        rhombus_type = input("what type of Rhombus:")
        if rhombus_type == "diamond": #checks if rhombus type is diamond
            mid = int (input("how long is the middle of the Rhombus:"))
            for i in range(mid):
                print(" " * (mid - i - 1) + ((str(Key_desired + " "))) * (i + 1))
            for e in range(mid, 0, -1):
                print(" " * (mid - e) + ((str(Key_side_desired + " "))) * (e))
            rhombus_height = mid * 2
            area = mid*rhombus_height // 2 + mid 
            print("the Diamond Rhombus area is", area)
            return shape_type
        if rhombus_type == "right": #check if rhombus type is a right rhombus
            mid = int(input("Enter the size of the rhombus: "))
            for i in range(mid):
                print(" " * (mid - i - 1) + Key_desired * (i + 1))
            for e in range(mid - 2, -1, -1):
                print(" " * (mid - i - 1) + Key_side_desired * (e + 1))
            bottom_rhombus_part_area = (mid * mid / 2)
            top_rhombus_part_area = (mid * mid / 2) 
            area = top_rhombus_part_area + bottom_rhombus_part_area
            print("The right Rhombus area is:", area)
            return shape_type
        if rhombus_type == "regular": #checks if rhombus type is a regular rhombus
            mid = int(input("Enter the size of the rhombus: "))
            for i in range(mid):
                print(" " * (mid - i - 1) + (str(Key_desired + " ")) * (i + 1))
            for i in range(mid - 2, -1, -1):
                print(" " * (mid - i - 1) + (str(Key_side_desired + " ") * (i + 1)))
            rhombus_height = mid * 2
            area = mid*rhombus_height // 2
            print("The regular rhombus area is:", area)
            return shape_type
        else:
            print("invalid triangle type")
    if shape_type == "circle" and art_mode == "n": #checks if shape type is the circle
        exit()
    if shape_type == "kite":  #checks if shape type is kite 
        # user enters the center size of the kite
        kite_length = int(input("How long is the center of the Kite: "))

        # the Key_desired is the character used for the kite

    # prints the upper half and the center of the kite
        for i in range(kite_length):
            print(" " * (kite_length - i - 1) + (Key_desired + " ") * (i + 1))
    # prints the lower half of the kite
        for i in range(kite_length,  0, -3):
            print(" " * (kite_length - i) + (Key_side_desired  + " ") * i)
        print("Kite!")
        return shape_type
    else:
        print("invalid shape type")

    #Art Mode

#this try block try's the functions to determine and to prevent a error from coming up
#if something was inputted incorrectly then the try block will say either Multiple patterns, A letter or number was entered in the wrong location or something was defined in the wrong location.
'''
this function is used to prepare for creation of tags for each shape in infinite mode basically what happends is the first
letter of a shape will be the leading letter of the tag it useful becauase it makes shapes avalible to be different sizes without having to re run the program 
and the tag number will be how many shapes of one type will be created.
the tags will be there own object.
'''
'''
this function infinite mode is a  expanded version of shape_function_design function basically
this function detects if art mode is activated. Once art mode is activated it will ask how many times the shape will run
with the __init__  function inside of infinite mode they will work together to create tags
tags are shorten versions of the shape name so they can be sorted from each other easily
this is how it works
so a for loop will loop thorugh the amount of times the shape is requested for
each shap will have a different tag
so if it was a square and the shape amount is 5 it would print out as: s1, s2, s3, s4, s5
it returns art_mode which is what the shapes is returned as to print.
'''
def infinite_mode(art_mode):
    class shapes:
        '''
        this function is used to prepare for creation of tags for each shape in infinite mode basically what happends is the first
        letter of a shape will be the leading letter of the tag it useful becauase it makes shapes avalible to be different sizes without having to re run the program 
        and the tag number will be how many shapes of one type will be created.
        the tags will be there own object.
        '''
        def __init__(self, shape_type, shapeshape_amount):
            self.shape_class = shape_class
            self.shape_amount = shape_amount
    if art_mode == "y":
        print("Infinite Has Been Activated-------")
        shape_amount = int (input("how many of this shape:"))#how many of the one shape will infinite mode go for 
        for i in range(shape_amount):

                shape_class = input("Enter shape type:") #shape type 
                shape_of_one = []
                class_defined = shapes(shape_class, shape_amount)
                shape_of_one.append(class_defined.shape_class)
                shape_of_one.append(class_defined.shape_amount)
                leading_letter = shape_of_one[0][0]
                number_max = shape_of_one[-1]
                combined_list = [] # creates combined list
                for number in range(number_max): #adds number and leading letter to ist 
                    number = str(number) #turns number into string
                    combine_create = leading_letter+number #combines leading letter and the number
                    combined_list.append(combine_create) #appends combinedd
                tuple_storage = (tuple(combined_list)) #turns combined list into tuple 
                for  tags in combined_list: #goes through each tag 
                    print("the height of the shape is used for parallelogram and squares!")
                    print("the width of the shape is used for rhombus, triangles, circles, squares, parallelograms, kites, and arrows")
                    height = int (input("height of this shape: \n "))
                    width  = int (input("width of this shape: \n"))
                    if leading_letter == "s":
                        for e in range(height):
                            print(str(Key_desired * width))
                        area = width * height
                        print("this square area is", area)
                        print("this square tag is", tags)                    
                    if leading_letter == "p": #checks if leading letter is p
                        for i in range(height):  
                            print(" " * (width - i - 1) + (str(Key_desired) * (width)))
                        print("Parallelogram!")
                    if leading_letter == "r": #checks if leading letter is r
                        print("rhombus types are diamond, regular, and right rhombus!")
                        rhombus_type = input("what type of Rhombus:")
                        if rhombus_type == "diamond": #checks if rhombus type is diamond
                            mid = int (input("how long is the middle of the Rhombus:"))
                            for i in range(width):
                                print(" " * (width - i - 1) + ((str(Key_desired + " "))) * (i + 1))
                            for e in range(width, 0, -1):
                                print(" " * (width - e) + ((str(Key_side_desired + " "))) * (e))
                            rhombus_height = width * 2
                            area = width*rhombus_height // 2 + mid 
                            print("the Diamond Rhombus area is", area)
                        if rhombus_type == "right": #checks if rhombus type is right
                            mid = int(input("Enter the size of the rhombus: "))
                            for i in range(width):
                                print(" " * (width - i - 1) + Key_desired * (i + 1))
                            for e in range(width - 2, -1, -1):
                                print(" " * (width - i - 1) + Key_side_desired * (e + 1))
                            bottom_rhombus_part_area = (width * width / 2)
                            top_rhombus_part_area = (width * width / 2) 
                            area = top_rhombus_part_area + bottom_rhombus_part_area
                            print("The right Rhombus area is:", area)
                        if rhombus_type == "regular": #checks if rhombus type is regular 
                            mid = int(input("Enter the size of the rhombus: "))
                            for i in range(mid):
                                print(" " * (mid - i - 1) + (str(Key_desired + " ")) * (i + 1))
                            for i in range(mid - 2, -1, -1):
                                print(" " * (mid - i - 1) + (str(Key_side_desired + " ") * (i + 1)))
                            rhombus_height = mid * 2
                            area = mid*rhombus_height // 2
                        if rhombus_type == "diamond": #checks if rhombus type is diamond
                            for i in range(width):
                                print(" " * (width - i - 1) + ((str(Key_desired + " "))) * (i + 1))
                            for e in range(width, 0, -1):
                                print(" " * (width - e) + ((str(Key_side_desired + " "))) * (e))
                            rhombus_height = width * 2
                            area = width*rhombus_height // 2
                            print("the Rhombus area is", area)

                    if leading_letter == "a": #checks if shape type is arrow
                        for r in range(width):
                            print(" " * (width- r - 1) + ((str(Key_desired + " " ))) * (r + 1))
                        for e in range(width - 1):
                            print(" " * (width - e - 1) + ((str(Key_side_desired + " " ))) * (e + 1))
                    if leading_letter == "t": #checks if shape type is triangle
                        print("Triangle options are: Right, Obtuse, Isoceles and Equilateral: \n")
                        triangle_type = input("What type of triangle:")
                        if triangle_type == "obtuse": #checks if trianlgle type is obtuse
                            for t in range(width):
                                print(" " * (width + t - 1) + (str(Key_desired)) * (t + 1))
                        print("this obtuse triangle tag is", tags)  
                        right = 1
                        if triangle_type == "right": #checks if triangle type is right
                            for t in range((int(width) + (int(right)))):
                                print(Key_desired * t)
                            area = width**2 / 2
                            print("this right triangle tag is", tags)     
                            print("Right triangle total key amount is:", area)
                        if triangle_type == "equilateral": #checks if triangle type is equilateral 
                            for i in range(width):
                                print(" " * (width - i - 1) + ((str(Key_desired + " "))) * (i + 1))
                            area = (math.sqrt(3) / 4) * bottom_leg ** 2
                            print("this equilateral triangle tag is", tags)     
                            print("Equilateral triangle area is:", area)
                        if triangle_type == "isoceles": #checks if trianlge type is isoceles
                            for i in range(width):
                                spaces = ' ' * (width - i - 1)
                                keys_part = Key_desired * (2 * i + 1)
                                print(spaces + keys_part + spaces)
                            area = (1/2) * bottom_leg * bottom_leg
                            print("this isoceles triangle tag is", tags)     
                            print("Isoceles triangle area is", area)
                    if leading_letter == "k": #checks if leading letter is k
                        for i in range(width):
                            print(" " * (width - i - 1) + (Key_desired + " ") * (i + 1))
                            # prints the lower half of the kite
                        for i in range(width,  0, -3):
                            print(" " * (width - i) + (Key_side_desired  + " ") * i)
                    if leading_letter == "c": #checks if leading letter is c
                        cir = width
                        radius = cir // 2 #to turn the circumference into radius by dividing by 2
                        (draw_circle(radius))
                        area_circle = pi * radius**2
                        area_circle_rounded = round(area_circle, 3)
                        print("the area of the circle is", area_circle_rounded)
                print("Shape tags are:") 
                print(tuple_storage)
                return art_mode #art mode is returned


#this try block tries the functions to determine and to prevent an error from coming up
#if something was inputted incorrectly then the try block will say either Multiple patterns, A letter or number was entered in the wrong location or something was defined in the wrong location.
try:
    (shape_fuction_design(shape_type))
    (infinite_mode(art_mode))
except UnboundLocalError:
    print("Multiple paterns were inputted")
except ValueError:
    print("A letter or number was entered in the wrong location!")
except NameError:
    print("something was defined incorrectly")
except RecursionError:
    print("the Functions may have had mixed matched with each other")