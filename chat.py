import openai

# Put your own generated openai-api-key
openai.api_key = "API KEY"


def chat(query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}]
    )

    return response.choices[0].message.content


# print(chat('Tell me about Diabetes')) /// Testing Code
