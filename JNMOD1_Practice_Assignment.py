# 1) Accept the user's first and last name and print them in 
#   reverse order with a space between them
first_name = input("Input your First Name: ")
last_name = input("Input your Last Name: ")

print("\nHello {} {}".format(last_name, first_name))


# 2) Accept an integer (n) and compute the value of n+nn+nnn
n_number = str(input("Input an Integer: "))
nn_number = n_number * 2
nnn_number = n_number * 3
total_n_value = int(n_number) + int(nn_number) + int(nnn_number)
print(total_n_value)


# 3) Ask the user "What country are you from?" then print the following
# statement: "I have heard that [input] is a beautiful country"
user_country = input("What country are you from?: ")

print("\nI have heard that {} is a beautiful country!".format(user_country))


# 4) What is the output of the following Python code
x = 10
y = 50
if (x ** 2 > 100 and y < 100):
    print(x, y)
'''Result:
    10 50'''


# 5) What is the output of the following addition (+) operator, and why does
# code chunk execute this way?
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)

'''Result:
>>> print(a)
[10, 20, 30, 40]
>>> print(b)
[10, 20, 30, 40]
'''
# The (+) operand in this code section appends the list of data to the existing 
# array of data. The reason this section of code runs this way is because in python,
# variables are more like pointers to a specific memory address, so when
# b appends more data, the address is changed and a is pointing to the
# address, so both show the same data when printed out


# 6) what is the output of the following code and what arithmetic operators is being used here?
print(2%6)
# Answer: 2, this is because the % operand basically returns the remainder of the quotient of 2/6, 
# but since 6 cannot be divided into 2 any whole number of times, the remainder would be 2


# 7) What is the output of the following code and what arithmetic operators are used here?
print(2 * 3 ** 3 * 4)
# The result is 216 and the multiplication and exponential operands are being used


# 8) What is a text editor


# 9) What is Python?


# 10)What is jupyter notebook, what type of python environment is it, and what alternatives
# are there to jupyter notebook?