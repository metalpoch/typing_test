"""
Perform typing speed test with this code

AUTHOR: Keiber Urbila
CREATE DATE: 12/05/2021
"""

from os import path, system
from time import time
from random import randrange
from difflib import SequenceMatcher as SM


BASE_DIR = path.abspath(path.dirname(__file__))


def language_selection() -> str:
    """Return language selected for user"""
    print("Select a language: ")
    print("(en) - English")
    print("(es) - Spanish")

    option = input("R: ")

    if option in ["en", "es"]:
        system('clear')
        return path.join(BASE_DIR, f"sentences_{option}.txt")
    else:
        exit("Goodbye!")


def get_score(sentences: str, response: str, time: float) -> str:
    """Get score for user"""
    score = SM(None, sentences, response).ratio() * 100
    score = round(score, 2)
    return f"Your perfection score was {score}% in a time of {time} seconds"


def get_number_line(selected_file: str) -> int:
    """ Return a int with the number line from sentences.txt """
    with open(selected_file) as f:
        return sum(1 for line in f)

def main():
    while True:
        selected_file = language_selection()
        number_line = get_number_line(selected_file)
        with open(selected_file) as f:
            sentences = f.readlines()[randrange(0, number_line)].rstrip("\n")

        print(f"Write the next sentences:\n    {sentences}\n")
        start_time = time()
        response = input("R: ")
        end_time = round(time() - start_time, 2)

        score = get_score(sentences, response, end_time)
        print(f"\n{score}\n")


if __name__ == "__main__":
    main()
