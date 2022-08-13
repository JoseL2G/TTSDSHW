# Data Structures Excersises

# Exercises 1)
from audioop import reverse
import math

def main():
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 1))

    int_list = input("Please enter a list of space separated integers: ")
    print(list_to_tuple_hash(int_list))

    list1, list2 = [3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]
    print(combine_list_evenNodd(list1, list2))

    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    print(reverse_divideTo(sample_list, 3))
    

# Exercise 1
def solve_quadratic(a_var, b_var, c_var):
    a, b, c = a_var, b_var, c_var

    positive_solution = ((-b) + math.sqrt((b**2) - 4 * a * c)) / 2
    negative_solution = ((-b) - math.sqrt((b**2) - 4 * a * c)) / 2

    return (positive_solution,negative_solution)


# Exercise 2
def list_to_tuple_hash(int_list):
    int_tuple = tuple(int_list.split())
    print(int_tuple)
    
    return hash(int_tuple)


# Exercise 3.
# Takes two lists, returns third with list1 odd and list2 evens index elements
def combine_list_evenNodd(list1, list2):
    stitches_list = []
    longest_list_length = 0

    # longest_list_length 
    list1_length, list2_length = len(list1), len(list2)
    longest_list_length = 0 
    if list1_length > list2_length:
        longest_list_length = list1_length
    else:
        longest_list_length = list2_length
        
    # For loops combines list1 odd elements and list2 even elements
    for i in range(longest_list_length):
        if i % 2 == 0: 
            stitches_list.append(list2[i])
        else:
            stitches_list.append(list1[i])

    return stitches_list


# Exercise 4.  
def reverse_divideTo(original_list, num_of_sections):
    og_list, sections = original_list, num_of_sections
    new_list = []
    temp_list = []
    section_length = len(og_list)/sections
    sect_count = 0

    for ele in og_list:
        temp_list.append(ele)
        sect_count += 1

        if sect_count == section_length:
            sect_count = 0
            new_list.append(reverse_list(temp_list))
            temp_list = []

    return new_list


def reverse_list(lst):
    original_list = lst
    reversed_list = []
    n_count = len(original_list) - 1
    
    while n_count > -1:
        reversed_list.append(original_list[n_count])
        n_count -= 1
        
    return reversed_list


if __name__ == "__main__":
    main()