nric = input('Enter an NRIC number: ')
possibleStartingLetters = ("T", "S", "F", "G")

if (nric.upper().startswith(possibleStartingLetters)) and (
len(nric) == 9) and (nric[1:8].isdigit()) and (nric[8:].isalpha()):
    digitWeight = [2, 7, 6, 5, 4, 3, 2]
    digits = list()
    for i in nric[1:8]:
        digits.append(int(i))
    combined = (a*b for a,b in list(zip(digits, digitWeight)))
    sumOfDigits = sum(combined)
    if (nric[0] in "TGtg"):
        sumOfDigits += 4
    quotient, remainder = divmod(sumOfDigits, 11)
    ST = ["J", "Z", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    FG = ["X", "W", "U", "T", "R", "Q", "P", "N", "M", "L", "K"]
    if (nric[0] in "STst") and (nric.endswith(ST[remainder])):
        print("NRIC is valid.")
    elif (nric[0] in "FGfg" and (nric.endswith(ST[remainder]))):
        print("NRIC is valid.")
    else:
        print("NRIC is invalid.")
else:
    print("NRIC is invalid.")