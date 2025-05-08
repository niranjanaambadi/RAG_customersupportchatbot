import os
from openai import OpenAI
from generator.prompt_template import build_prompt

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question, context_chunks):
    context = "\n".join(context_chunks)
    prompt = build_prompt(context, question)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()