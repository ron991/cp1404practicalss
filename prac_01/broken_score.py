"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# I've been taught to use def main or def whatever you want to name it function
# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    while score <= 0:
        print("Invalid score")
        score = float(input("Enter score: "))
        if score < 50:
            print("Bad")
        elif score > 50:
            print("Passable")
        elif score > 90:
            print("Excellent")
        else:
            print("invalid score")


main()
