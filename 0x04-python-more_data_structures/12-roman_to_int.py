#!/usr/bin/python3

def roman_to_int(roman_string: str) -> int:
    """Function that converts a Roman numeral to an integer

    Args:
        roman_string: roman numeral string
    Return:
        integer representation of roman numeral string or 0
    """
    romanNumeralDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                        'M': 1000}
    number = 0
    if (type(roman_string) is not str or roman_string is None):
        return number
    RNStrList = list(enumerate(roman_string))
    for i, s in RNStrList:
        currentNumber = romanNumeralDict[s]
        # print("Current number before comparison {:d}".format(currentNumber))
        currentLetterIndex = i
        if currentLetterIndex + 1 < len(RNStrList):
            nextLetterIndex = currentLetterIndex + 1
            # print("Next letter index {:d}".format(nextLetterIndex))
            nextLetter = RNStrList[nextLetterIndex][1]
            nextNumber = romanNumeralDict[nextLetter]
            # print("next number {:d}".format(nextNumber))
            if currentNumber < nextNumber:
                # convert current number to a negative number
                currentNumber *= -1
                # print("Current number is {:d}".format(currentNumber))
        number += currentNumber
        # print(number)

    return number
