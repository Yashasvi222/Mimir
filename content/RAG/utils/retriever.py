import numpy as np

def topk(query, data, k: int=5) -> list:
    cosine_similarities = []
    for idx, row in data.iterrows():
        dot_product = np.dot(query, np.array(list(map(float, "".join(map(lambda s: s.replace("\n", ""), row.embeddings.strip("[]").split(","))).split()))))
        query_ = np.linalg.norm(query)
        emb_ = np.linalg.norm(np.array(list(map(float, "".join(map(lambda s: s.replace("\n", ""), row.embeddings.strip("[]").split(","))).split()))))
        cosine_similarity = dot_product / (query_*emb_ + 10**-5)
        cosine_similarities.append((idx, cosine_similarity))
    cosine_similarities.sort(key=lambda x: x[1], reverse=True)
    indexes = [x[0] for x in cosine_similarities[:k]]
    return indexes

#np.array(list(map(float, "".join(map(lambda s: s.replace("\n", ""), query.strip("[]").split(","))).split())))