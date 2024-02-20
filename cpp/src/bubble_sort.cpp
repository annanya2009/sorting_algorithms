#include <iostream>
#include "../include/common_vars.h"
#include <utility> // for std::swap

int main() {

    // Start at 1 because i keeps track of counting which iteration we are in
    for (int i = 1; i < my_vector_size; i++){

        // Start at 0 because it is used to index within the array
        for (int j = 0; j < my_vector_size - 1; j++){

            // Swap adjacent values if left is greater than right
            if (my_vector[j] > my_vector[j+1]){
                std::swap(my_vector[j], my_vector[j+1]);
            }
            }
        }

    print_int_vector(my_vector);

    return 0;
    
    }
