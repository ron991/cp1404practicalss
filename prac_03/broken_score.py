"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


# I've been taught to use def main or def whatever you want to name it function

def main():
    score = get_score()
    while score < 0:
        print("Invalid score")
    if score < 50:
        print("Bad")
    elif score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("invalid score")


def get_score():
    score = float(input("Enter score: "))
    return score


print(random.randint(0, 101))
main()
