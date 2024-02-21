#include <iostream>
#include "../include/common_vars.h"

int main() {

    // Start at 1 because want to skip the first element
    for (int i = 1; i < my_vector_size; i++){

        // Remove value from vector and store in temp
        int temp = my_vector[i];
        my_vector.erase(my_vector.begin()+i);

        // Start checking from the end of the sorted array
        int left_idx_of_sorted = i - 1;

        // Go through sorted array
        while (temp < my_vector[left_idx_of_sorted]){

            // Update iterator of sorted array
            left_idx_of_sorted -= 1;
        }

        // Place temp value in sorted array
        auto it = my_vector.begin() + (left_idx_of_sorted+1);
        my_vector.insert(it, temp);
        
    }

    print_int_vector(my_vector);

    return 0;
    
    }