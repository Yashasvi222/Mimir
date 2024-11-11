import pandas as pd
from content.RAG.assets.data import data
from preprocess import vectorizer, cleaner


if __name__ == "__main__":
    data = cleaner(data)
    embeddings = vectorizer(data)

    for text, emb in zip(data, embeddings):
        print(text, emb)
        break

    df = pd.DataFrame(tuple(zip(data, embeddings)), columns=['text', 'embeddings'])
    df.to_csv('./database.csv', index=False)