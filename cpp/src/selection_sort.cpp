#include "../include/common_vars.h" // for unsorted_array
#include <iostream>
#include <utility> // for std::swap

int main() {

    /**Starts at 0 because going to be used to index and ends early because no other elements 
     * to compare for last element */
    for (int i = 0; i < my_vector_size - 1; i++){

        // Reset the local minimum for the unsorted array to it's first element
        int local_min_index = i+1;

        // Starts 1 element offset of sorted array because that is where unsorted array starts
        for (int j = i+1; j < my_vector_size; j++){

            if (my_vector[local_min_index] > my_vector[j]){
                local_min_index = j;
            }
        }

        /* Replace the last value of unsorted array with local min
        NOTE : swap() takes values of similar type */
        std::swap(my_vector[i], my_vector[local_min_index]);

    }

    print_int_vector(my_vector);
    
    return 0;
}