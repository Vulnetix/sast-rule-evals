import logging
try:
    raise ValueError("test")
except ValueError:
    logging.exception("Error occurred", exc_info=False)

