# At least 1 letter between [a-z] and 1 letter between [A-Z]
# At least 1 number between [0-9]
# At least 1 character from [$#@]
import re

def exercise2_function():
    acceptableNums, acceptableSpecChars = [str(i) for i in range(10)], ['$', '#', '@']
    userPassword = input("Input your password: ")

    print(re.match(r'\w',userPassword)

    while len(userPassword) < 6 or len(userPassword) > 16:
        print('''Password is too long or too short.\n
            please enter a password between 6 and 16 characters''')
        userPassword = input("Input your password: ")


exercise2_function()
    
