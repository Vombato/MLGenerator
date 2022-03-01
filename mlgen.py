import random

def getMLPhrase(wordlist):
    msg = ""
    cong = ["e", "o", "se", "ma", "in", "da", "per", "su"]
    for n in range(random.randint(3, 10)):
        sub = random.choice(wordlist)
        ind = random.randint(1, 7)
        if n % ind == 0:
            if n == 0:
                msg += random.choice(cong)
            else:
                msg += " " + random.choice(cong)
        else:
            msg += " " + sub
    msg += "."
    return msg.capitalize()


def main():
    my_file = open("parole.txt", "r")
    data = my_file.read()
    list = data.split("\n")
    print(getMLPhrase(list))


if __name__ == "__main__":
    main()
