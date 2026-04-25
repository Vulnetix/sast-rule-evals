import re

text = "hello world"
result = re.sub("hello", "world", text)  # RUF055: plain string could use str.replace
