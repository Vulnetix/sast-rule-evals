# vnx-llm-006 eval target
import openai
import sqlite3

client = openai.OpenAI()
conn = sqlite3.connect("app.db")
cursor = conn.cursor()

# TRIGGERS: LLM output interpolated into SQL via f-string
def natural_language_query(user_question):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Convert the user question to a SQL WHERE clause only."},
            {"role": "user", "content": user_question},
        ]
    )
    llm_sql_fragment = response.choices[0].message.content
    # DANGER: LLM output directly in SQL
    cursor.execute(f"SELECT * FROM products WHERE {llm_sql_fragment}")
    return cursor.fetchall()

# TRIGGERS: SQL via string concatenation with LLM output
def query_by_llm_output(question):
    llm_output = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    ).choices[0].message.content
    cursor.execute("SELECT * FROM users WHERE name = " + llm_output + " LIMIT 10")
    return cursor.fetchall()

# Safe alternative: use parameterized queries and allowlisted fields
# cursor.execute("SELECT * FROM products WHERE category = ?", (validated_category,))
