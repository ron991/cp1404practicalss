"""" "The program allows the user to enter the number of items and the price of each different item. Then the program
computes and displays the total price of those items. If the total price is over $100, then a 10% discount is applied
to that total before the amount is displayed on the screen.""

Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92

"""


# I've been taught to use def main or def whatever you want to name it function
def main():
    # total price is 0
    # get input price from user
    total_price = 0
    number_of_items = int(input("Please enter number of items : "))
    # error check for items
    while number_of_items < 0:
        print("Invalid amount of items")
        number_of_items = int(input("Please enter number of items : "))
    for i in range(number_of_items):
        price_of_item = float(input("Please enter price per item"))
        while number_of_items < 0:
            print("Invalid amount of items")
            number_of_items = int(input("Please enter number of items : "))
        for i in range(number_of_items):
            price_of_item = float(input("Please enter price per item"))
            total_price = price_of_item
        if total_price > 100:
            total_price *= 0.9  # apply 10% discount

        print("Total price for ", number_of_items, " items is $", total_price, sep='')

        # with string formatting for currency output
        print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))

    # I tried but how I wanted to do it didn't work see below
    #    initial_price = price_of_item

    # if initial_price > 100:
    #    reduced_price = initial_price * 0.10
    #    total_price = initial_price - reduced_price
    #
    #    print("Your total price for",number_of_items, "items is $", total_price)


main()
