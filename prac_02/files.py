def main():
    out_file = open("name.txt", "w")
    name_input = input("Please enter your name: ")
    print(name_input, file=out_file)
    out_file.close()

    in_file = open("name.txt", "r")
    name_input = in_file.read().strip()
    in_file.close()
    print("Your name is", name_input)

    out_file = open("numbers.txt", "w")
    numbers = 17, "\n", 42, "\n", 400

    in_file = open("numbers.txt", "r")
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    in_file.close()
    print(number1 + number2)

    in_file = open("numbers.txt", "r")
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    in_file.close()
    print(total)


main()
