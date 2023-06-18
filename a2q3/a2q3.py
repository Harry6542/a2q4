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