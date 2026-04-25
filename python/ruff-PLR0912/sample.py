# Sample for Ruff rule PLR0912: too-many-branches
# This file is designed to trigger the PLR0912 rule.
# Run: ruff check --select PLR0912 <this_file>

def capital(country):
    if country == "Australia":
        return "Canberra"
    elif country == "Brazil":
        return "Brasilia"
    elif country == "Canada":
        return "Ottawa"
    elif country == "England":
        return "London"
    elif country == "France":
        return "Paris"
    elif country == "Germany":
        return "Berlin"
    elif country == "Poland":
        return "Warsaw"
    elif country == "Romania":
        return "Bucharest"
    elif country == "Spain":
        return "Madrid"
    elif country == "Thailand":
        return "Bangkok"
    elif country == "Turkey":
        return "Ankara"
    elif country == "United States":
        return "Washington"
    else:
        return "Unknown"  # 13th branch
