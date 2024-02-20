#!/usr/bin/env python3
import json

def read_array_from_json_file(file_path, array_name):
    '''
    Extracts array from specified json file.

    Parameters
    - file_path: string 
        Specifies file path to the json file
    - array_name: string
        Specifies the name of the array you are trying to extract from json file
    
    Returns
    Array with array_name in specified json file path.
    '''
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data[array_name]