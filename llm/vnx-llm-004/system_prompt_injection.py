# vnx-llm-004 eval target
import openai

client = openai.OpenAI()

# TRIGGERS: user input interpolated into system prompt via f-string
def chat_with_user_context(user_input, language_preference):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a helpful assistant. Always respond in {language_preference}. User context: {user_input}"},
            {"role": "user", "content": "Hello"},
        ]
    )
    return response.choices[0].message.content

# TRIGGERS: Anthropic system= parameter with f-string
import anthropic

def summarize_with_context(user_query, context):
    anth_client = anthropic.Anthropic()
    message = anth_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=f"Summarize content for: {user_query}",
        messages=[{"role": "user", "content": context}]
    )
    return message.content

# Safe alternative: keep system prompts static
# {"role": "system", "content": "You are a helpful assistant."}
