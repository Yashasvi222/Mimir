from nerd import read_tad, read_abstract, read_conclusion
from content.llm import three_elements, zero_shot_learning, one_shot_learning, few_shot_learning
from extractor import extract_text_from_pdf, extract_specific_sections, save_sections_to_files
import google.generativeai as genai


def trigger(pdf_path, approach):
    extracted_text = extract_text_from_pdf(pdf_path, line_spacing_threshold=0.5, paragraph_spacing_threshold=20)
    sections = extract_specific_sections(extracted_text)
    save_sections_to_files(sections)

    genai.configure(api_key="AIzaSyA6LITghBDg-Y5c-38vIcu6nFcD5J92KhQ")
    model = genai.GenerativeModel("gemini-1.5-pro")

    path_tad = "title_and_authors.txt"
    path_abstract = "abstract_and_introduction.txt"
    path_conclusion = "conclusion.txt"

    corpus_tad = read_tad(path_tad)
    corpus_abstract = read_abstract(path_abstract)
    corpus_conclusion = read_conclusion(path_conclusion)

    tad = three_elements(corpus_tad, model)
    if approach == "zsl":
        abstract, conclusion = zero_shot_learning(corpus_abstract, corpus_conclusion, model)  # one of the approaches
    elif approach == "osl":
        abstract, conclusion = one_shot_learning(corpus_abstract, corpus_conclusion, model)  # one of the approaches
    elif approach == "fsl":
        abstract, conclusion = few_shot_learning(corpus_abstract, corpus_conclusion, model)  # one of the approaches
    elif approach == "rag":
        abstract, conclusion = zero_shot_learning(corpus_abstract, corpus_conclusion, model)  # one of the approaches

    author, title, year = tad.split("||")

    return year, author, title, abstract, conclusion
