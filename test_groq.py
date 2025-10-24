import openai

client = openai.OpenAI(
    api_key="your-groq-api-key",
    base_url="https://api.groq.com/openai/v1"
)

response = client.responses.create(
    model="llama-3.3-70b-versatile",
    input="Tell me a fun fact about the moon in one sentence.",
)

print(response.output_text)