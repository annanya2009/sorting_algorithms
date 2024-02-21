#!/usr/bin/env python3
from tools import common_funcs

# define global vars
path_to_shared_vars = 'tools/common_vars.json'
unsorted_array = common_funcs.read_array_from_json_file(file_path=path_to_shared_vars, array_name="my_array")
unsorted_array_len = len(unsorted_array)

# start at 1 to skip first value
for i in range(1, unsorted_array_len):
    temp = unsorted_array.pop(i)
    last_idx_of_sorted = i - 1

    # Go through sorted array
    while temp < unsorted_array[last_idx_of_sorted]:
        
        # update
        last_idx_of_sorted -= 1

        # Once it gets to last element, break
        if last_idx_of_sorted == -1:
            break
    
    # Place temp value within sorted array
    unsorted_array.insert(last_idx_of_sorted+1, temp)

print(unsorted_array)

    
