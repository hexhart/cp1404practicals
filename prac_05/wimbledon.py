"""
CP1404/CP5632 Practical 5 By Hexon Hartley Jimenez
Wimbledon - Game, Set, Match program
Estimated: 30 minutes
Actual: 1 hour 3 minutes
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Read FILENAME to obtain the data to process and display"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:  # read csv file with encoding UTF-8
        in_file.readline()  # Read next line
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    champion_to_count = {}  # new dictionary for champion's count
    countries = set()
    for score in records:
        countries.add(score[INDEX_COUNTRY])
        try:
            champion_to_count[score[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[score[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    sorted_champions = sorted(champion_to_count.items())  # additional feature, soft champions in alphabetical order
    for name, count in sorted_champions:
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
