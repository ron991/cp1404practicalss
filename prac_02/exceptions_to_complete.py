"""
CP1404/CP5632 - Practical - Suggested Solution
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
