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
def test_partB():
    def test_lsdict():
        tests_ran = 0
        fails = 0
        case1 = []
        case2 = [{"a": 30,
                  "b": 50},
                 {}]
        case3 = [{"a": 90,
                  "b": 19},
                 {"a": 20,
                  "b": 12}]
        test_case = [
            {"input": case1,
             "output": deep_copy_list_of_dicts(case1),
             "reason": "Empty list should not impact function success"},
            {"input": case2,
             "output": deep_copy_list_of_dicts(case2),
             "reason": "Dict with one internal blank dict should still be able to be copied"},
            {"input": case3,
             "output": deep_copy_list_of_dicts(case3),
             "reason": "References should be different for internal dicts too"}
        ]
        for test in test_case:
            # Testing references to differ
            if test["input"] is test["output"]:
                fails += 1
                print("Test Deep Copy \nERROR: References are the same\n", test)
            # Lists should still be equal
            if test["input"] != test["output"]:
                fails += 1
                print("Test Deep Copy \nERROR: Values are not the same\n", test)
            # Changing list test["input"] should not impact list in test["output"]
            test["input"].append({"z": 9})
            if test["input"] == test["output"]:
                fails += 1
                print("Test Deep Copy \nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"].pop()
            # Just ran 3 tests
            tests_ran += 3
            # Checking internal dicts are also deep copied
            if len(test["input"]) > 0 and len(test["input"][-1]) > 0:
                tests_ran += 1
                test["input"][-1]["z"] = 8
                if test["input"] == test["output"]:
                    fails += 1
                    print("Test Deep Copy \nERROR: Inner list values should no longer be the the same\n", test)
                # reset test["input"]
                test["input"][-1].pop("z")
        return tests_ran, fails

    def test_remove():
        tests_ran = 0
        fails = 0
        case1 = [[], [4]]
        case2 = [[1, 2, 3], [45, 2, 14], [78, 47, 3, 56], [9, 3, 7]]
        case3 = [[1, 2, 1], [1, 2, 3], [1, 23, 4], [1, 21]]
        test_case = [
            {"input": (case1, 4),
             "output": remove_from_2DList(case1, 4),
             "reason": "Empty list should not impact function success"},
            {"input": (case1, 2),
             "output": remove_from_2DList(case1, 2),
             "reason": "Removing value that does not exist should not impact function success"},
            {"input": (case2, 3),
             "output": remove_from_2DList(case2, 3),
             "reason": "Lists of different sizes should not impact function success"},
            {"input": (case3, 1),
             "output": remove_from_2DList(case3, 1),
             "reason": "Internal lists should not impact function success"}
        ]
        for test in test_case:
            # Testing references should be same
            if test["input"][0] is not test["output"]:
                fails += 1
                print("Test Remove \nERROR: References are not the same\n", test)

            # Lists should still be equal
            if test["input"][0] != test["output"]:
                fails += 1
                print("Test Remove \nERROR: Values are not the same\n", test)

            # Changing list test["input"] should impact list in test["output"]
            test["input"][0].append([3])
            if test["input"][0] != test["output"]:
                fails += 1
                print("Test Remove \nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"][0].pop()

            # Value should be removed from inner lists
            for inner in test["output"]:
                if test["input"][1] in inner:
                    fails += 1
                    print("Test Remove \nERROR: \n", test, "In internal list(s):\n", inner)

            # Just ran 4 tests
            tests_ran += 4
            # Checking internal lists are also shallow copied
            if len(test["input"][0]) > 0 and len(test["input"][0][0]) > 0:
                tests_ran += 1
                test["input"][0][0].append(8)
                if test["input"][0] != test["output"]:
                    fails += 1
                    print("Test Remove \nERROR: Inner list values should be the the same\n", test)
                # reset test["input"][0]
                test["input"][0][0].pop()
        return tests_ran, fails

    def test_filter():
        tests_ran = 0
        fails = 0
        case1 = [[], [4]]
        case2 = [[1, 2, 3], [45, 2, 14], [78, 47, 3, 56], [9, 3, 7]]
        case3 = [[1, 2, 1], [1, 2, 3], [3, 23, 4], [1, 1]]
        test_case = [
            {"input": (case1, 4),
             "output": filter_from_2DList(case1, 4),
             "reason": "Empty list should not impact function success"},
            {"input": (case1, 2),
             "output": filter_from_2DList(case1, 2),
             "reason": "Removing value that does not exist should not impact function success"},
            {"input": (case2, 3),
             "output": filter_from_2DList(case2, 3),
             "reason": "Lists of different sizes should not impact function success"},
            {"input": (case3, 1),
             "output": filter_from_2DList(case3, 1),
             "reason": "Internal lists should not impact function success"}
        ]
        for test in test_case:
            # Testing references should not be same
            if test["input"][0] is test["output"]:
                fails += 1
                print("Test Filter \nERROR: References are the same\n", test)

            # Changing list test["input"] should not impact list in test["output"]
            test["input"][0].append([3])
            if test["input"][0] == test["output"]:
                fails += 1
                print("Test Filter \nERROR: Outer list values should no longer be the the same\n", test)
            # Reset test["input"]
            test["input"][0].pop()

            # Value should be removed from inner lists
            for inner in test["output"]:
                if test["input"][1] in inner:
                    fails += 1
                    print("Test Filter \nERROR: \n", test, "In internal list(s):\n", inner)

            # Just ran 4 tests
            tests_ran += 4

            # Checking internal lists are also different references
            if len(test["input"][0]) > 0 and len(test["input"][0][-1]) > 0:
                tests_ran += 1
                test["input"][0][-1].append(8)
                if test["input"][0] == test["output"]:
                    fails += 1
                    print("Test Filter \nERROR: Inner list values should not be the the same\n", test)
                # reset test["input"][-1]
                test["input"][0][-1].pop()
        return tests_ran, fails

    lsdict_ran, lsdict_fail = test_lsdict()
    rm_ran, rm_fail = test_remove()
    filt_ran, filt_fail = test_filter()
    return lsdict_ran + rm_ran + filt_ran, lsdict_fail, rm_fail, filt_fail
def run_tests(run_all=False):
    def stats(Arun, Als, Adict, Brun, Bcp, Brm, Bflt):
        print("Total Tests Ran: ", Arun + Brun)
        print("PartA Tests Ran: ", Arun)
        print("PartA Fails:", Als + Adict)
        print("\t List of List Fails:", Als)
        print("\t Dict of Dicts Fails:", Adict)
        print("PartB Tests Ran: ", Brun)
        print("PartB Fails:", Bcp + Brm + Bflt)
        print("\t List of Dicts Fails:", Bcp)
        print("\t Remove From List Of List Fails:", Brm)
        print("\t Filter List Of List Fails:", Bflt)
        exit()

    PartARan, PartA_ls, PartA_dict = test_partA()
    if run_all:
        PartBRan, PartB_dpcp, PartB_rm, PartB_filt = test_partB()
        stats(PartARan, PartA_ls, PartA_dict, PartBRan, PartB_dpcp, PartB_rm, PartB_filt)
    if PartA_ls > 0:
        print("FINISH copy_list_of_lists BEFORE GOING ON")
        print("copy_list_of_lists HAS: ", PartA_ls, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    if PartA_dict > 0:
        print("FINISH copy_dict_of_dicts BEFORE GOING ON")
        print("copy_dict_of_dicts HAS: ", PartA_dict, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    PartBRan, PartB_dpcp, PartB_rm, PartB_filt = test_partB()
    if PartB_dpcp > 0:
        print("FINISH deep_copy_list_of_dicts BEFORE GOING ON")
        print("deep_copy_list_of_dicts HAS: ", PartB_dpcp, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    if PartB_rm > 0:
        print("FINISH remove_from_2DList BEFORE GOING ON")
        print("remove_from_2DList HAS: ", PartB_rm, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    if PartB_rm > 0:
        print("FINISH filter_from_2DList BEFORE GOING ON")
        print("filter_from_2DList HAS: ", PartB_filt, "FAILS")
        print("DON'T FORGET TO COMMIT")
        exit()
    else:
        stats(PartARan, PartA_ls, PartA_dict, PartBRan, PartB_dpcp, PartB_rm, PartB_filt)


if _name_ == '_main_':
    # TODO - Run to see what is working
    run_tests()

