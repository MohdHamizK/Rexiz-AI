from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="Your OpenAI API_KEY", 
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
