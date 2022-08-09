# Data Structures Excersises

# Exercises 1)
import math

def main():
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 1))

    int_list = input("Please enter a list of space separated integers: ")
    print(list_to_tuple_hash(int_list))

    list1, list2 = [3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]
    print(combine_list_evenNodd(list1, list2))

    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    print(reverse_divideTo(sample_list, 2))
    

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
    list1_length = len(list1)
    list2_length = len(list2)
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
# Slice a list into 3 equal parts and reverse each list
def reverse_divideTo(lst, num_of_sections):
    original_list = lst
    divided_list = []
    list_total_length = len(lst)
    sections = num_of_sections
    temp_section_list = []

    for i in num_of_sections:
        







    

if __name__ == "__main__":
    main()