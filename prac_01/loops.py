# I've been taught to use def main or def whatever you want to name it function

def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    for i in range(20, 1, -1):
        print(i, end=' ')
    print()

    number_of_stars = int(input("Please enter a value for stars : "))
    for i in range(number_of_stars):
        print('*', end=' ')
    print()

    for i in range(1, number_of_stars + 1):
        print('*' * i)
    print()


main()
