"""
CP1404/CP5632 Practical 5 By Hexon Hartley Jimenez
State names in a dictionary
File needs reformatting
Estimated: 20 minutes
Actual: 45 minutes
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        if state_code in CODE_TO_NAME:
            print(f"{state_code} is {CODE_TO_NAME[state_code]}")
            print("Exiting Program\n")
            break
        else:
            print("Invalid short state")
            state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Error occurred: Invalid Input")

print("List of State Codes:")
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:3} is {state_name}")
