import os
import openai

api_endpoint = "https://api.openai.com/v1/chat/gpt"
api_key = os.getenv("GPT_KEY")
print(api_key)


def gpt(qt):
    openai.api_key = os.getenv("GPT_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=qt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]
