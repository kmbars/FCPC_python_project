
user_name_1 = input ("Enter Your Name: ")
print (user_name_1)
result = ""

for x in range(len(user_name_1)):
    char = user_name_1 [x]

    if char == "A":
        result += "B"

    elif char == "B":
        result += "C"

    elif char == "C":
        result += "D"

    elif char == "E":
        result += "F"

    elif char == "G":
        result += "H"

    elif char == "I":
        result += "J"

    elif char == "K":
        result += "L"

    elif char == "M":
        result += "N"

    elif char == "O":
        result += "P"

    elif char == "Q":
        result += "R"

    elif char == "S":
        result += "T"

    elif char == "U":
        result += "V"

    elif char == "W":
        result += "X"

    elif char == "Y":
        result += "Z"

    else:
        char += result


    print (result,end='')

