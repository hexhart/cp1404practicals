"""
CP1404/CP5632 Practical 6 By Hexon Hartley Jimenez
Intermediate Exercise: Programming languages client code file
Estimated: 30 minutes
Actual:
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Main function of the programming language"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)

main()
