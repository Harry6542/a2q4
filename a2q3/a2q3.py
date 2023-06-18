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
