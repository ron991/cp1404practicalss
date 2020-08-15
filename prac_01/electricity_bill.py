
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

# I've been taught to use def main
def main():
    tariff_choice = input(
        "Electricity Bill Estimator 3.0""\n""What tariff do you fall under: ""\n""(A) Tariff 11""\n""(B)"
        " Tariff 31""\n""(Q) Quit")
    while tariff_choice != "q":
        if tariff_choice == "a":
            tariff_choice_11 = float(input("Enter Cents per kWh: "))
            tariff_choice_11_per_daily_use = float(input("Enter daily use in kWh"))
            tariff_choice_11_billing_days = int(input("Enter number amount of days: "))
            tariff_choice_11_bill = tariff_choice_11 * tariff_choice_11_per_daily_use * tariff_choice_11_billing_days
            print("Estimated bill: ", tariff_choice_11_bill)
            tariff_choice = input(
                "Electricity Bill Estimator 3.0""\n""What tariff do you fall under: ""\n""(A) Tariff 11""\n""(B)"
                " Tariff 31""\n""(Q) Quit")
        elif tariff_choice == "b":
            tariff_choice_31 = float(input("Enter Cents per kWh: "))
            tariff_choice_31_per_daily_use = float(input("Enter daily use in kWh"))
            tariff_choice_31_billing_days = int(input("Enter number amount of days: "))
            tariff_choice_31_bill = tariff_choice_31 * tariff_choice_31_per_daily_use * tariff_choice_31_billing_days
            print("Estimated bill: ", tariff_choice_31_bill)
            tariff_choice = input(
                "Electricity Bill Estimator 3.0""\n""What tariff do you fall under: ""\n""(A) Tariff 11""\n""(B)"
                " Tariff 31""\n""(Q) Quit")
        else:
            print("Invalid option, Please try again")
            tariff_choice = input(
                "Electricity Bill Estimator 3.0""\n""What tariff do you fall under: ""\n""(A) Tariff 11""\n""(B)"
                " Tariff 31""\n""(Q) Quit")

    if tariff_choice == "q":
        print("Thank you for using Electricity Bill Estimator 3.0 ")


main()
