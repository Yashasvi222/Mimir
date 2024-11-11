import spacy
from sentence_transformers import SentenceTransformer

nlp = spacy.load('en_core_web_sm')

def cleaner(data):
    # Process the input text with spaCy
    doc = nlp(data)
    # Extract sentences as strings
    sentences = [sent.text for sent in doc.sents]
    return sentences

def vectorizer(data):
    # Load the SentenceTransformer model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    # Encode the list of sentences
    data = model.encode(data)
    return data