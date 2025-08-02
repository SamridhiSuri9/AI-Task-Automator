import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def summarize_text(text, max_tokens=500):
    prompt = (
        "Summarize the following text into concise bullet points suitable for a student presentation:\n\n"
        + text[:3000]
    )
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content
