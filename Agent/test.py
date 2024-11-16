import openai

openai.api_key = "sk-pd4kVZOzY3xWw4xL0ALayEjjWBJ0kLUGT4gXvAymsGMDr7YM"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "你好，今天的天气怎么样？"}
    ]
)

print(response.choices[0].message['content'])