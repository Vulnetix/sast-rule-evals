import sys

def process_input(user_data):
    # VNX-PY-002: eval() with user input
    result = eval(user_data)
    return result

def run_code(code_string):
    # VNX-PY-002: exec() with dynamic code
    exec(code_string)
