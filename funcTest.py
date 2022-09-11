# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


sample_input = 'HACK 2'
edited_input = sample_input.split()

def input_permutations(input_list):
    sorted_list = [*input_list[0]]
    sorted_list.sort()
    
    list_permutations = list(permutations(sorted_list, int(input_list[1])))
    
    for i in list_permutations:
        print('')
        for j in range(int(input_list[1])):
            print(i[j],end='')

input_permutations(edited_input)