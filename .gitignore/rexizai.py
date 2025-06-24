from openai import OpenAI
from openai import OpenAIError
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)
try:
    response = client.chat.completions.create(
    model="openai/gpt-4o",
    messages=[
        {"role": "user", "content": "Hello, are you working?"}
    ],
    max_tokens=500  # ✅ Set to something reasonable like 300–1000
)

    print("✅ API key is working. Response:")
    print(response.choices[0].message.content)
    
except OpenAIError as e:
    print(f"❌ OpenAI API error: {e}")
except Exception as e:
    print(f"⚠️ General error: {e}")
