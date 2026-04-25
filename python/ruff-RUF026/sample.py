from collections import defaultdict

d = defaultdict(default_factory=list)  # RUF026: use defaultdict(list) not default_factory kwarg
