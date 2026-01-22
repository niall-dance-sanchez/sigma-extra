from flask import Flask, request
from leaderboard_functions import load_people, save_people

api = Flask(__name__)


@api.route("/", methods=["GET"])
def index():
    return {
        "title": "Ben's Mean, Competitive API",
        "description": "He wants to win."
    }


@api.route("/person", methods=["GET"])
def person_index():
    """Returns a list of person details."""
    if request.method == "GET":
        return load_people()

    data = request.json
    people = load_people()
    people.append(data)
    save_people(people)

    return data


if __name__ == "__main__":

    api.run(debug=True, port=3000)
