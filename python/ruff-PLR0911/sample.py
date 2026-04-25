# Sample for Ruff rule PLR0911: too-many-return-statements
# This file is designed to trigger the PLR0911 rule.
# Run: ruff check --select PLR0911 <this_file>

def capital(country: str) -> str | None:
    if country == "England":
        return "London"
    elif country == "France":
        return "Paris"
    elif country == "Poland":
        return "Warsaw"
    elif country == "Romania":
        return "Bucharest"
    elif country == "Spain":
        return "Madrid"
    elif country == "Thailand":
        return "Bangkok"
    else:
        return None
