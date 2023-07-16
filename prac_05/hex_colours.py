"""
CP1404/CP5632 Practical 5 By Hexon Hartley Jimenez
Hexadecimal colour program
Estimated: 30 minutes
Actual: 5 hours 3 minutes
"""

COLOUR_CODES = {"Amber": "#ffbf00", "apricot": "#fbceb1", "aqua": "#00ffff", "azure1": "#f0ffff", "azure2": "#e0eeee",
                "azure3": "#c1cdcd", "azure4": "#838b8b", "beaver": "#9f8170", "beige": "#f5f5dc", "black": "#000000"}

uppercase_keys = [key.title() for key in COLOUR_CODES.keys()]
display_colour_selection = ','.join(uppercase_keys)
print(f"Colors Available: {display_colour_selection}")

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        colour_code = COLOUR_CODES[colour_name]
        print(f"The code for {colour_name.title()} is {colour_code.upper()}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()
