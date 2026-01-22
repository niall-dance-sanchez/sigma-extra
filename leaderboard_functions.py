import json
from datetime import date
from dateutil import


def save_people(people: list[dict]) -> None:
    """Save the data to a file called stories.json"""

    with open("stories.json", "w") as f:
        json.dump(people, f, indent=4)


def load_people() -> list[dict]:
    """Load the stories from a file called stories.json"""

    with open("people.json", "r") as f:
        data = json.load(f)

    return data


def get_date_of_birth(date_string: str) -> date:
    """Returns a DOB from an awkward string"""
    chunks = date_string.split("-")
    dob = [int(v) for v in chunks]
    dob = date(*dob)
    return dob


def is_over_thirtenn(dob: date) -> bool:

    today = date.today()
    thirteen_dob = today - r


def is_a_valid_person(potential_person: dict) -> bool:
    """Returns true if the object is valid."""

    for k in ["name", "date_of_birth", "verified"]:
        if k not in potential_person:
            return False

    today = date.today()
    dob = get_date_of_birth(potential_person["date_of_birth"])
    age = today - dob

    return True
