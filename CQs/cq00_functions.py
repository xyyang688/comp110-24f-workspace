"""Welcome my cq00!"""

__author__ = "730809746"


""""The function aims to take your input and repeat it back to you"""


def mimic(message: str) -> str:
    return message


"""The function aims to print the result of calling mimic"""


def main() -> None:
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
