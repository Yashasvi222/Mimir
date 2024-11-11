from langchain_community.llms import Ollama

def prompt(query, context):
    prompt = f"""
    Context: {context}

    Query: {query}

    Provide an answer based on the above context.
    """
    ollama = Ollama(base_url="http://localhost:11434", model="mistral")
    response = ollama.invoke(prompt)
    return response