def main():
    password_checker = get_password()
    for i in range(len(password_checker)):
        print("*", end='')


def get_password():
    password_checker = input("Please enter your password ")
    return password_checker


main()
