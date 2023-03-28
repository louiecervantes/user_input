import openai

import openai
import os

openai.api_key = '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'

def ask_question(question):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

question = "Describe the 3 best performing machine learning algorithms"
answer = ask_question(question)
print(f"Q: {question}\nA: {answer}")

