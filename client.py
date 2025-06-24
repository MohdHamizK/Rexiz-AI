from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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", 
)

command = client.chat.completions.create(
  model="openai/gpt-4o",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Rexiz skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ],
  max_tokens=500
)

print(command.choices[0].message.content)