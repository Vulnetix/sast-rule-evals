# Fake vulnerable code for SAST evaluation - DO NOT USE IN PRODUCTION
# This file demonstrates VNX-PY-015: Python ReDoS via user-controlled regular expression

import re
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search')
def search():
    pattern = request.args.get('pattern', '')
    text = request.args.get('text', '')

    # VULNERABLE: user-controlled input compiled as regex pattern
    # Attacker can supply (a+)+ to cause catastrophic backtracking
    compiled = re.compile(request.args.get('pattern'))
    result = compiled.match(text)
    return jsonify({'matched': result is not None})

@app.route('/filter', methods=['POST'])
def filter_data():
    data = request.form.get('data', '')
    pattern = request.form.get('regex', '')

    # VULNERABLE: user-controlled pattern in re.match
    match = re.match(request.form['regex'], data)

    # VULNERABLE: user pattern in re.search
    found = re.search(request.args.get('find'), data)

    return jsonify({'result': bool(match)})
