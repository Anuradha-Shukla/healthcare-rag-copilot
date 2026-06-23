from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6Ja22N3YtFShetq0CJ1IHg_jfR6-PH5iIkwEAAfd9yevQ"
)


def generate_answer(question, context):

    prompt = f"""
Context:
{context}

Question:
{question}

Answer only using the context.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
