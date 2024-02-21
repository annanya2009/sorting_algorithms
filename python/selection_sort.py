#!/usr/bin/env python3
from tools import common_funcs

# Define global vars
path_to_shared_vars = 'tools/common_vars.json'
unsorted_array = common_funcs.read_array_from_json_file(file_path=path_to_shared_vars, array_name="my_array")
unsorted_array_len = len(unsorted_array)

# Start at 0 since i will be used for indexing
for i in range(0, unsorted_array_len-1):

    # Start initial estimate of lowest valuue to the start of unsorted array 
    loc_min_idx = i+1

    # Go through unsorted array
    for j in range(i+1, unsorted_array_len):

        # Check if estimate is lower than the rest of the unsorted array
        if unsorted_array[loc_min_idx] > unsorted_array[j]:
            loc_min_idx = j

    # Swap lowest value in unsorted array with last value in sorted array
    unsorted_array[i], unsorted_array[loc_min_idx] = unsorted_array[loc_min_idx], unsorted_array[i]

# Display result
print('sorted array : ', unsorted_array)