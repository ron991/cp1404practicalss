# I've been taught to use def main or def whatever you want to name it function
def main():
    # get choice from user
    menu_choice = input("Please choose from the menu: ""\n""(A) Count in evens""\n" "(B) Count in Odds"
                        "\n""(C) Squared numbers""\n""(Q) Quit")

    # If user hasn't picked quit, display other options
    while menu_choice != "q":
        if menu_choice == "a":
            number_range_start = int(input("Please enter a number"))
            number_range_finish = int(input("Please enter the 2nd number"))
            for i in range(number_range_start, number_range_finish, 2):
                print(i, end=' ')
        elif menu_choice == "b":
            number_range_start = int(input("Please enter a number"))
            number_range_finish = int(input("Please enter the 2nd number"))
            for i in range(number_range_start, number_range_finish, 2):
                print(i, end=' ')

        # Need help , I don't know how to do this , the solution isn't posted in the extended work
        elif menu_choice == "c":
            number_range_start = int(input("Please enter a number"))
            number_range_finish = int(input("Please enter the 2nd number"))
            for i in range(number_range_start, number_range_finish):
                print(i**2, end=' ')


main()
