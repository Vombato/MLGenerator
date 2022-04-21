# pylint: disable=missing-module-docstring
# pylint: disable=C0116
import random
import string


def get_ml_phrase(wordlist):
    msg = ""
    cong = ["e", "o", "se", "ma", "in", "da", "per", "su", "di", \
        "con", "sul", "dal", "il", "lo", "la", "i", "gli", "le"]
    ind = random.randint(2, 9)
    for num in range(random.randint(3, 25)):
        sub = get_word(wordlist)
        if random.randint(0, 10) == 0:
            sub = add_remove_random_letters(sub)
        if num % ind == 0:
            if num == 0:
                msg += get_word(cong)
            else:
                msg += " " + get_word(cong)
        else:
            msg += " " + sub
    msg += "."
    return msg.capitalize()


def add_remove_random_letters(word):
    if random.randint(0, 1) == 0:
        word = word[:random.randint(0, len(word)-1)] + random.choice(string.ascii_letters) \
            + word[random.randint(0, len(word)-1):]
        return word + random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", \
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
    return word[:-random.randint(1,2)]

def get_word(wordlist):
    return random.choice(wordlist)

def main():
    with open("parole.txt", "r", encoding="utf-8") as my_file:
        data = my_file.read()
        word_list = data.split("\n")
        print(get_ml_phrase(word_list))

if __name__ == "__main__":
    main()
