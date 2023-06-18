# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    31 May 2023
#
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Debugging exercise, relevant to Chapter 3 and 7
###############################################################################

# TODO: Fill in your information below
# Student Name-Harry Patel
# NSID-ozc189
# Student Number-1135887

# Recall another name for a list of dictionaries is a record.
import copy


def copy_list_of_lists(data: list) -> list:
    new_list = []
    for sublist in data:
        new_sublist = sublist.copy()
        new_list.append(new_sublist)
    return new_list
def copy_dict_of_dicts(data: dict) -> dict:
    new_dict = {}
    for key, value in data.items():
        if isinstance(value, dict):
            new_dict[key] = copy_dict_of_dicts(value)  # Recursively copy nested dictionaries
        else:
            new_dict[key] = value  # Copy non-dictionary values
    return new_dict
def deep_copy_list_of_dicts(data: list) -> list:
    new_list = []
    for item in data:
        new_dict = {}
        for key, value in item.items():
            if isinstance(value, dict):
                new_dict[key] = value.copy()
            else:
                new_dict[key] = value
        new_list.append(new_dict)
    return new_list
def remove_from_2DList(arr, value):
    # Iterate over the outer list in reverse order
    for i in range(len(arr) - 1, -1, -1):
        inner_list = arr[i]

        # Check if the value exists in the inner list
        if value in inner_list:
            # Remove the value from the inner list
            inner_list.remove(value)

            # Check if the inner list becomes empty after removing the value
            if not inner_list:
                # Remove the inner list from the outer list
                arr.remove(inner_list)
    return arr

def filter_from_2DList(data: list, val) -> list:
    new_list = []
    for sublist in data:
        new_sublist = [element for element in sublist if element != val]
        new_list.append(new_sublist)
    return new_list
def test_partA():
    def test_ls():
        tests_ran = 0
        fails = 0
        # Empty List
        case1 = []
        case2 = [[], [3]]
        case3 = [[1, 2, 3, 5], ["a", "b", "c", "f"]]
        test_case = [
            {"input": case1,
             "output": copy_list_of_lists(case1),
             "reason": "Empty list should not impact functions success"},
            {"input": case2,
             "output": copy_list_of_lists(case2),
             "reason": "List with one internal list empty should still be able to be copied"},
            {"input": case3,
             "output": copy_list_of_lists(case3),
             "reason": "References should be different since it is a list of lists"}
        ]
        for test in test_case:
            # Testing references to differ
            if test["input"] is test["output"]:
                fails += 1
                print("Test List Copy\nERROR: References are the same\n", test)
            # Lists should still be equal
            if test["input"] != test["output"]:
                fails += 1
                print("Test List Copy\nERROR: Values are not the same\n", test)
            # Changing list test["input"] should not impact list in test["output"]
            test["input"].append([-1, 2, 4])
            if test["input"] == test["output"]:
                fails += 1
                print("Test List Copy\nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"].remove([-1, 2, 4])

            # Just ran 3 tests
            tests_ran += 3

            # Checking internal lists are also deep copied
            if len(test["input"]) > 0 and len(test["input"][0]) > 0:
                tests_ran += 1
                popped = test["input"][-1].pop()
                if test["input"] == test["output"]:
                    fails += 1
                    print("Test List Copy\nERROR: Inner list values should no longer be the the same\n", test)
                # reset test["input"]
                test["input"][-1].append(popped)
        return tests_ran, fails

    def test_dict():
        tests_ran = 0
        fails = 0
        # Empty List
        case1 = {}
        case2 = {"a": {},
                 "b": {1: -1,
                       2: -2}}
        case3 = {"a": {1: 0,
                       2: 1,
                       3: 2},
                 "b": {1: -1,
                       2: -2}}
        test_case = [
            {"input": case1,
             "output": copy_dict_of_dicts(case1),
             "reason": "Empty dict should not impact function success"},
            {"input": case2,
             "output": copy_dict_of_dicts(case2),
             "reason": "Dict with one internal blank dict should still be able to be copied"},
            {"input": case3,
             "output": copy_dict_of_dicts(case3),
             "reason": "References should be different for internal dicts too"}
        ]
        for test in test_case:
            # Testing references to differ
            if test["input"] is test["output"]:
                fails += 1
                print("Test Dict Copy\nERROR: References are the same\n", test)
            # Lists should still be equal
            if test["input"] != test["output"]:
                fails += 1
                print("Test Dict Copy\nERROR: Values are not the same\n", test)
            # Changing list test["input"] should not impact list in test["output"]
            test["input"]["c"] = {"z": 9}
            if test["input"] == test["output"]:
                fails += 1
                print("Test Dict Copy\nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"].pop("c")

            # Just ran 3 tests
            tests_ran += 3

        # Checking internal lists are also deep copied
        tests_ran += 1
        case3["a"][1] = 9
        if case3 == test_case[2]["output"]:
            fails += 1
            print("Test Dict Copy\nERROR: Inner dict values should no longer be the the same\n", test)
        # reset case3
        case3["a"][1] = 0
        return tests_ran, fails

    ls_ran, ls_fail = test_ls()
    dict_ran, dict_fail = test_dict()
    return ls_ran + dict_ran, ls_fail, dict_fail


