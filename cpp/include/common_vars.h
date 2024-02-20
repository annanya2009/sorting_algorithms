#include <vector>
#include <iostream>

std::vector<int> my_vector = {2, 8, 5, 3, 9, 4, 1};
int my_vector_size = my_vector.size();

void print_int_vector(std::vector<int> temp_vec){
    for (int i = 0; i < temp_vec.size(); i++){
        std::cout << temp_vec[i] << std::endl;
    }
}