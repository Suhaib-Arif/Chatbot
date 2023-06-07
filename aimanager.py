import openai
import logging

user_key = "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"
openai.api_key = user_key


def QueryResponse(answer1, answer2, question1, question2):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role" : "system", "content": "You are a Medical Bot that gives medical advice based on the questions asked"},
            {"role": "assistant", "content": question1},
            {"role": "user", "content": answer1},
            {"role": "assistant", "content": question2},
            {"role": "user", "content": answer2},
        ],
        max_tokens=100
    )

    reply = response['choices'][0]["message"]["content"]

    return reply