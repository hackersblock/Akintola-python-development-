from google import genai

client = genai.Client(api_key="AIzaSyD1f-eqKrVByKboDHiB3-ISgj1n3KrPGoI")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)