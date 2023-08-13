"""
CP1404/CP5632 Practical 10 by Hexon Hartley Jimenez
Wikipedia API & Python Library experimentation
"""
import wikipedia

search_keyword = input("Enter a page title or search phrase: ")
page = wikipedia.page(search_keyword)
print(f"Searched Title: {page.title}")
print(f"\nSummary{page.summary}")
print(f"\n{page.url}")

