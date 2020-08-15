"""CP1404/CP5632 - Practical Answer the following questions:
1. When will a ValueError occur? #If you don't enter in
a number
2. When will a ZeroDivisionError occur? #when the denominator is 0

3. Could you change the code to avoid the
possibility of a ZeroDivisionError? #Create a while loop for a number input above 0. """

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator != 0:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Finished.")
