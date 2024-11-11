def read_tad(path):
    tad = ""
    with open(path, "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                tad += " "
                tad += stripped_line
    return tad


def read_conclusion(path):
    conclusion = ""
    with open(path, "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                conclusion += " "
                conclusion += stripped_line
    return conclusion


def read_abstract(path):
    abstract = ""
    with open(path, "r") as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line:
                abstract += " "
                abstract += stripped_line
    return abstract


if __name__ == "__main__":
    ...


