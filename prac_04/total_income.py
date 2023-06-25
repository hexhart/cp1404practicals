"""
CP1404/CP5632 - Practical 4 By Hexon Hartley Jimenez
Starter code for cumulative total income program
"""


# How do you add values to a list?
# Answer: By creating an empty list via defining a variable = []

# How many loops will we need? What kind of loops?
# Definite loops based on user input, hence For Loop will be used.

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):  # enumerate(sequence, start) replaces previous For loop
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}      Total: ${total:10.2f}")


main()
