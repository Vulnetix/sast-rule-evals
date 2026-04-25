# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-LLM-002: LLM output passed to code execution (RCE)

import openai
import subprocess
import os

client = openai.OpenAI(api_key="sk-test1234567890abcdef")

def execute_llm_code(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message.content

    # VULNERABLE: LLM output passed directly to eval()
    result = eval(content)
    return result

def run_llm_command(task):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Generate a shell command to: {task}"}]
    )
    content = response.choices[0].message.content

    # VULNERABLE: LLM output passed to os.system
    os.system(content)

def process_llm_script(code_request):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": code_request}]
    )
    # VULNERABLE: executing LLM generated code
    exec(response.choices[0].message.content)
