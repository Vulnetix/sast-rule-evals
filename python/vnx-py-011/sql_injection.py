# VNX-PY-011: Python SQL injection
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

user_input = "admin"
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
cursor.execute("SELECT * FROM users WHERE id = %s" % user_input)
