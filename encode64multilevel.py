import base64
import sys


if len(sys.argv) < 3:
    print("Usage: python script_name.py <string_to_encode> <number_of_levels>")
    sys.exit(1)

strToBeEncoded = sys.argv[1]
noOfLevels = int(sys.argv[2])

def getBase64(strToBeEncoded):
    return base64.b64encode(strToBeEncoded.encode("ascii")).decode("ascii")

def getUrlSafeBase64(strToBeEncoded):
    return base64.urlsafe_b64encode(strToBeEncoded.encode("ascii")).decode("ascii")

def getCustomBase64(strToBeEncoded):
    
    encoded = base64.b64encode(strToBeEncoded.encode("ascii")).decode("ascii")
    return encoded.replace('+', '-').replace('/', '_')

def getWorstCaseBothSides(strToBeEncoded, index, encoding_type="standard"):
    beginAt = 0
    if index == 1:
        beginAt = 2             
        strToBeEncoded = "x" + strToBeEncoded
    elif index == 2:
        beginAt = 3
        strToBeEncoded = "xx" + strToBeEncoded

    strLength = len(strToBeEncoded)
    endAt = strLength * 4 // 3

    if encoding_type == "standard":
        encoded_str = getBase64(strToBeEncoded)
    elif encoding_type == "urlsafe":
        encoded_str = getUrlSafeBase64(strToBeEncoded)
    elif encoding_type == "custom":
        encoded_str = getCustomBase64(strToBeEncoded)
    else:
        raise ValueError("Unknown encoding type")

    return encoded_str[beginAt:endAt + 1]

def joinArrToString(arrToBeJoined):
    return "|".join(arrToBeJoined)

def getWorstCaseAtLevel(arrOfStrToBeEncoded, encoding_type):
    posibilities = []
    for strToBeEncoded in arrOfStrToBeEncoded:
        for i in range(3):
            posibilities.append(getWorstCaseBothSides(strToBeEncoded, i, encoding_type))
    return posibilities

def getWorstCases(strToBeEncoded, noOfLevels):
    arrOfEncodedLevels = []
    arrOfStrToBeEncoded = [strToBeEncoded]
    encoding_types = ["standard", "urlsafe", "custom"]

    for encoding_type in encoding_types:
        x = []
        arrOfStrToBeEncoded = [strToBeEncoded]  
        for s in range(noOfLevels):
            x = getWorstCaseAtLevel(arrOfStrToBeEncoded, encoding_type)
            arrOfEncodedLevels.append(f"{encoding_type} Level {s+1}: " + joinArrToString(x))
            arrOfStrToBeEncoded = x
    return arrOfEncodedLevels

a = getWorstCases(strToBeEncoded, noOfLevels)
for encoded_level in a:
    print(encoded_level)
