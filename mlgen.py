# pylint: disable=missing-module-docstring
import random


def get_ml_phrase(wordlist):
    msg = ""
    cong = ["e", "o", "se", "ma", "in", "da", "per", "su"]
    for num in range(random.randint(3, 10)):
        sub = random.choice(wordlist)
        ind = random.randint(1, 7)
        if num % ind == 0:
            if num == 0:
                msg += random.choice(cong)
            else:
                msg += " " + random.choice(cong)
        else:
            msg += " " + sub
    msg += "."
    return msg.capitalize()


def main():
    with open("parole.txt", "r", encoding="utf-8") as my_file:
        data = my_file.read()
        word_list = data.split("\n")
        print(get_ml_phrase(word_list))


if __name__ == "__main__":
    main()
