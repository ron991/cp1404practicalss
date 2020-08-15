"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


# I've been taught to use def main or def whatever you want to name it function
def main():
    # input sales from user
    sales = float(input("Enter sales: "))
    while sales == "" or sales < 0:
        print("Please enter a valid sales number")
        sales = float(input("Enter sales: "))
    if sales < 1000:
        ten_percent_bonus = sales * 0.1
        print("Your sales bonus is : ", sales + ten_percent_bonus)
    elif sales > 1000:
        fifteen_percent_bonus = sales * 0.15
        print("Your sales bonus is : ", sales + fifteen_percent_bonus)
    else:
        print("Invalid option")


main()
