from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_plan(task, repo_structure):
    prompt = f'''
You are a senior software engineer.

Task:
{task}

Repository:
{repo_structure}

Identify:
1. likely files
2. root cause
3. fix strategy
'''

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
