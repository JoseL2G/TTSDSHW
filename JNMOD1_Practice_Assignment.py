# 1. Accept the user's first and last name and print them in 
#   reverse order with a space between them
first_name = input("Input your First Name: ")
last_name = input("Input your Last Name: ")

print("\nHello {} {}".format(last_name, first_name))


# 2. Accept an integer (n) and compute the value of n+nn+nnn
n_number = str(input("Input an Integer: "))

nn_number = n_number * 2

nnn_number = n_number * 3

total_n_value = int(n_number) + int(nn_number) + int(nnn_number)

print(total_n_value)


# 3. Ask the user "What country are you from?" then print the following
# statement: "I have heard that [input] is a beautiful country"
user_country = input("What country are you from?: ")

print("I have heard that {} is a beautiful country!".format(user_country))

