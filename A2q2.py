###############################################################################
# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    31 May 2023
#
# All rights reserved.
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Testing; relevant to Chapter 5, 6, 7
###############################################################################

# TODO: Fill in your information below
# Name-Harry Patel
#NSID-ozc189
#student Number-Harry Patel
#Course-Harry Patel

################### DO NOT ALTER CODE BELOW ###################################
def gcd(val1: int, val2: int) -> int:
    """
    Purpose: Find the greatest common divisor (gcd) of the two values passed in.
    Pre-conditions:
        :param val1: int - integer value being compared to find gcd.
            Must be less than 1000, else returns -1
        :param val2: int - integer value being compared to find gcd
            Must be less than 1000, else returns -1
    Post Conditions:
        None
    Return:
        int - The greatest common positive divisor of the two numbers passed in.
            -1 returned on failure.
    """
    return -1
def replace(input_str: str, target: str, replacement: str) -> str:
    """
    Purpose: Replace all instances of target string with replacement string within input string.
        Starting at the first occurrence of target string.
    Pre-condition
        :param input_str:str - input string to change target strings to replacement strings
        :param target: str - string that one wishes to change, if empty will return original string uncahnged.
        :param replacement: str - string that will replace target strings in the input string
    Post Condition:
        None
    Return:
        str - new string where target strings have been changed to replacement string
    """
    new_str = ""
    inp_len = len(input_str)
    targ_len = len(target)
    if inp_len < targ_len or targ_len==0:
        new_str = input_str
    else:
        i = 0
        while i < inp_len:
            if input_str[i:i+targ_len] == target:
                new_str += replacement
                i += targ_len
            else:
                new_str += input_str[i]
                i += 1
    return new_str


def grade_letter(score:int) -> str:
    """
    Purpose: Get the grade letter related to the score passed in.

    Pre-condition
        :param score:int - the number being calculated to a letter grade.
            Should be within the range of 0-100
    Post Condition:
        None
    Return:
        str - string associated with the score passed in
            if score is outside valid range returns the string "Invalid"
    """
    letter = ""
    if score < 0 or score > 100:
        letter = "Invalid"
    elif score >= 90:
        letter = "A"
    elif score >= 80:
        letter = "B"
    elif score >= 70:
        letter = "C"
    elif score >= 60:
        letter = "D"
    else:
        letter = "F"
    return letter

def sort_students_into_grades(student_list: list) -> dict:
    """
    Purpose: Goes through a list of dictionaries adding student names to the appropriate dictionary grade letter
        If the student's grade is not one of "A", "B", "C", "D", or "F", it is added to list "Invalid".
    Pre-condition:
        :param student_list: list of dictionaries,
            each dictionary represents a student and contains two keys: 'name' and 'grade'
    Post Condition:
        None
    Return:
        dict with lists as values; each key has a list value of names of students with that grade letter.
            Contains the keys "A","B","C","D","F","Invalid"
    """
    return {}
################### DO NOT ALTER CODE ABOVE ###################################
# TODO: Create tests for functions above
# TODO Create test driver for whitebox tested functions
# TODO: Create test driver for blackbox tested functions
# TODO: Create test driver to test all functions

# Creating tests for every functions above:
def test_gcd():
    test_cases = [
        # Test cases with valid inputs
        (10, 5, 5),  # GCD of 10 and 5 is 5
        (24, 36, 12),  # GCD of 24 and 36 is 12
        (81, 27, 27),  # GCD of 81 and 27 is 27

        # Test cases with invalid inputs
        (1000, 500, -1),  # Value exceeding the limit should return=-1
        (500, 1000, -1),  # Value exceeding the limit should return -1
    ]

    for val1, val2, expected in test_cases:
        result = gcd(val1, val2)
        if result == expected:
            print(f"PASS: gcd({val1}, {val2}) returned {result}")
        else:
            print(f"FAIL: gcd({val1}, {val2}) returned {result}, expected {expected}")
def test_replace():
    test_cases = [

        # Test cases with valid values
        ("Hello, World!", "o", "x", "Hellx, Wxrld!"),  # Replace "o" with "x"
        ("Mississippi", "ss", "pp", "Mippiippi"),  # Replace "ss" with "pp"
        ("OpenAI", "AI", "ChatGPT", "OpenChatGPT"),  # Replace "AI" with "ChatGPT"
        ("Hello, World!", "", "x", "Hello, World!"),  # Empty target, should return the original string

        # Test cases with invalid values
        ("Hello, World!", "loooong", "x", "Hello, World!"),  # Target not found
        ("Hello, World!", "o", "", "Hell, Wrld!"),  # Empty replacement

        # Edge case
        ("", "x", "y", ""),  # Empty input string
    ]

    for input_str, target, replacement, expected in test_cases:
        result = replace(input_str, target, replacement)
        if result == expected:
            print(f"PASS: replace('{input_str}', '{target}', '{replacement}') returned '{result}'")
        else:
            print(
                f"FAIL: replace('{input_str}', '{target}', '{replacement}') returned '{result}', expected '{expected}'")

def test_grade_letter():
    test_cases = [
        # Test cases with valid scores
        (95, "A"),  # Score of 95 should result in grade "A"
        (85, "B"),  # Score of 85 should result in grade "B"
        (75, "C"),  # Score of 75 should result in grade "C"
        (65, "D"),  # Score of 65 should result in grade "D"
        (55, "F"),  # Score of 55 should result in grade "F"

        # Test cases with invalid scores
        (-10, "Invalid"),  # Negative score should result in "Invalid"
        (110, "Invalid"),  # Score above 100 should result in "Invalid"

        # Edge cases
        (0, "F"),  # Minimum valid score
        (100, "A"),  # Maximum valid score
    ]

    for score, expected in test_cases:
        result = grade_letter(score)
        if result == expected:
            print(f"PASS: grade_letter({score}) returned '{result}'")
        else:
            print(f"FAIL: grade_letter({score}) returned '{result}', expected '{expected}'")
def test_sort_students_into_grades():