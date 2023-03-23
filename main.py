
import pandas as pd
import numpy as np
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

df = pd.read_csv("ubi.csv").dropna()

n = len(df)
idxes = list(range(n)) 
prompt = ""
for idx in idxes:
    question = df['Question'].iloc[int(idx)]
    answer = df['Answer'].iloc[int(idx)]

    if question.startswith(","):
        question = "Ubi" + question
    else:
        question = "Ubi " + question

    prompt += question + "\n" + answer + "\n"

prompt += "\nKeep listing ubi questions in the same format and styling. Pay attention to the rhymes and aliteration!\n"
output = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=512,
    temperature=0.7
)
print(output['choices'][0]['text'])
