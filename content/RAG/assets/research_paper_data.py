from nerd import read_tad, read_abstract, read_conclusion



if __name__ == "__main__":
    path_tad = "title_and_authors.txt"
    path_abstract = "abstract_and_introduction.txt"
    path_conclusion = "conclusion.txt"

    data_tad = read_tad(path_tad)
    data_abstract = read_abstract(path_abstract)
    data_conclusion = read_conclusion(path_conclusion)