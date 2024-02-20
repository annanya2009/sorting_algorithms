#!/usr/bin/env python3
from tools import common_funcs

# Define global vars
path_to_shared_vars = 'tools/common_vars.json'
unsorted_array = common_funcs.read_array_from_json_file(file_path=path_to_shared_vars, array_name="my_array")
unsorted_array_len = len(unsorted_array)


for i in range(1, unsorted_array_len):
    for j in range(0, unsorted_array_len-1):
        if unsorted_array[j] > unsorted_array[j+1]:
            unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]

# unsorted array is now sorted