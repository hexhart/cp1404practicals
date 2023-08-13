"""
CP1404/CP5632 Practical 10 by Hexon Hartley Jimenez
Wikipedia API & Python Library experimentation
"""
import wikipedia

search_keyword = input("Enter a page title or search phrase: ")
while search_keyword != "":
    try:
        page = wikipedia.page(search_keyword, auto_suggest=False)
        print(f"Searched Title: {page.title}")
        print(f"Summary:\n{wikipedia.summary(search_keyword, sentences=2)}")
        print(f"\nURL: {page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation page found. Suggestions:", e.options)
    except wikipedia.exceptions.PageError:
        print("Page not found.")

    search_keyword = input("\nEnter another page title or search phrase (blank to exit): ")
print("Exiting...")
print("Program Terminated")
