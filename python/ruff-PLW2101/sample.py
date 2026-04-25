import threading

with threading.Lock():  # PLW2101: lock created directly in with statement
    pass
