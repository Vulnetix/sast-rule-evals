# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-LLM-001: LLM prompt injection via user-controlled input

import openai

client = openai.OpenAI(api_key="sk-test1234567890abcdef")

def answer_question(user_input):
    # VULNERABLE: user input directly interpolated into system prompt via f-string
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. User context: {user_input}"},
            {"role": "user", "content": f"Answer this question: {user_input}"}
        ]
    )
    return response.choices[0].message.content

def handle_request(request):
    query = request.args.get("q", "")
    # VULNERABLE: prompt constructed by concatenating user input
    prompt = "Summarize the following: " + query
    result = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return result
