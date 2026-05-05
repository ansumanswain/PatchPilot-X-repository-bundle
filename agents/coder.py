from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_fix(task, code_context, failure_output=""):
    prompt = f'''
Task:
{task}

Code:
{code_context}

Failures:
{failure_output}

Fix the issue and return only code.
'''

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
