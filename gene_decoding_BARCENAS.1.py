CCS 1A Programming 2
CCS 1A
Due Nov 20, 12:00 PM
Challenge: Caesar Cipher
303030 points out of possible 30

Haisoj Nayahub
Nov 20
Using the pattern of Caesar Cipher, where A=B, B=C, C=D ....

Write a python code capable of conversion, with dynamic input.

Point System:

10 pts for input
20 pts for algorithm

Total of: 30 pts
This will serve as grade for Quiz. (LA)
Your work
Graded

gene_decoding_BARCENAS.1.py
Text

dynamic_input_BARCENAS.py
Text

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
gene_decoding_BARCENAS.1.py
Displaying gene_decoding_BARCENAS.1.py.
