"""
display menu
get choice
while choice != quit option
    if choice == first option
        do first task
    else if choice == <second option>
        do second task
    ...
    else if choice == <n-th option>
        do n-th task
    else
        display invalid input error message
    display menu
    get choice
do final thing, if needed
"""


# I've been taught to use def main or def whatever you want to name it function
def main():
    get_name = input("Please enter your name: ")
    print("Welcome ", get_name)
    choice = input(
        "Please choose from the following options : ""\n""(A)lpha""\n""(B)eta""\n""(Q)uit").isupper()
    while choice != "q":
        if choice == "a":
            print("Alpha")
            choice = input(
                "Welcome to the menu selector, Please choose from the following options : ""\n""(A)lpha""\n""(B)eta""\n""(Q)uit")
        elif choice == "b":
            print("Beta")
            choice = input(
                "Welcome to the menu selector, Please choose from the following options : ""\n""(A)lpha""\n""(B)eta""\n""(Q)uit")
        else:
            print("invalid option")
            choice = input(
                "Welcome to the menu selector, Please choose from the following options : ""\n""(A)lpha""\n""(B)eta""\n""(Q)uit")
    if choice == "q":
        print("Thanks for choosing the menu selector")


main()
