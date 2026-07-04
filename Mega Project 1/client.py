from openai import OpenAI
import os

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")  # read from environment variable
)

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # instead of gpt-3.5-turbo
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud...."},
        {"role": "user", "content": "what is coding?"}
    ]
)

print(completion.choices[0].message.content)
