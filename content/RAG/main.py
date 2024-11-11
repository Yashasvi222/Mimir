import pandas as pd
from utils.preprocess import cleaner, vectorizer
from utils.retriever import topk
from llm.llm import prompt





corpus = pd.read_csv("utils/database.csv")

query = input("Enter query: ")

cleaned = cleaner(query)
vector = vectorizer(cleaned)

indexes = topk(vector, corpus)

context = []
for i in indexes:
    context.append(corpus.iloc[i].text)
context = " ".join(context)

print("check")
response = prompt(query, context)
print(response)