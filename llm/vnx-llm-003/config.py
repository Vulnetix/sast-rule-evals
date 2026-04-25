# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-LLM-003: Hardcoded LLM API key

import openai
import anthropic

# VULNERABLE: hardcoded OpenAI API key
openai.api_key = "sk-proj-abcdefghijklmnopqrstuvwxyz1234567890ABCDEF"

# VULNERABLE: hardcoded Anthropic API key
ANTHROPIC_API_KEY = "sk-ant-api03-abcdefghijklmnopqrstuvwxyz1234567890"

# VULNERABLE: key hardcoded in client initialization
client = openai.OpenAI(api_key="sk-abcdefghijklmnop1234567890ABCDEFGHIJ")

anthropic_client = anthropic.Anthropic(
    api_key="sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXXXXX"
)
