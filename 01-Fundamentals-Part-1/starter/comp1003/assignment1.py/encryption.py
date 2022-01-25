# encryption using a linear feedback shift register
from bindec import *


# converts a character c into a list of six 1's and 0's using Base64 encoding
def charToBin(c):
    # converts a character into a list of six 1's and 0's using Base64 encoding
    binList=[]
    #A is 65 at Ascii and 0 at 64Base
    #ASCII value of uppercase alphabets – 65 to 90
    if c.isupper():
        chrToint = ord(c) - 65
        intToBin = decToBin(chrToint)
        print(intToBin)
        binList.append(intToBin)
        print(binList)
    else:
        chrToint = ord(c) - 26
        intToBin = decToBin(chrToint)
        print(intToBin)
        binList.append(intToBin)
        print(binList)

    
    return binList


# converts a list of six 1's and 0's into a character using Base64 encoding
def binToChar(b):
    binlist_toDec = binToDec(b)
    print(binlist_toDec)
    if binlist_toDec < 25 :
        intOfBin = binlist_toDec + 65
        print(intOfBin)
        intToChar = chr(intOfBin)
        print(intToChar)
        return intToChar
    else: 
        intOfBin = binlist_toDec + 71
        print(intOfBin)
        intToChar = chr(intOfBin)
        print(intToChar)
        return intToChar   
binToChar([1,0,1,1,1,0])


# convert a string of characters into a list of 1's and 0's using Base64 encoding
def strToBin(s):
    Values = []
    result= []
    for c in s:
        if c.isupper(): 
            asciivalueOf_C = ord(c)- 65
            Values.append(asciivalueOf_C)
        else: 
            asciivalueOf_C = ord(c)- 71
            Values.append(asciivalueOf_C)
    for v in Values:
        valueOfCH = decToBin(v)
        result.append(valueOfCH)
    print(result)

    return result
strToBin("Camera")
# convert a list of 1's and 0's into a string of characters using Base64 encoding
def binToStr(b_list):
    # Implement me
    return ""

# generates a sequence of pseudo-random numbers
def generatePad(seed, k, length):
    # Implement me
    return []

# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message, seed, k):
    # Implement me
    return ""
