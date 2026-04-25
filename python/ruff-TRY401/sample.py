import logging

try:
    int("abc")
except ValueError as e:
    logging.exception("Failed: %s", e)

