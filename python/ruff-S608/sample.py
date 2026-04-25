# Sample for Ruff rule S608: hardcoded-sql-expression
# This file is designed to trigger the S608 rule.
# Run: ruff check --select S608 <this_file>

def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = " + str(user_id))  # S608: SQLi

