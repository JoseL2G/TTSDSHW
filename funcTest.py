def exercise2_function():
    acceptableNums, acceptableSpecChars = [str(i) for i in range(10)], ['$', '#', '@']
    userPassword = input("Input your password: ")

    while len(userPassword) < 6 or len(userPassword) > 16:
        print("Password is too short or too long")