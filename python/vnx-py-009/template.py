from jinja2 import Environment

# VNX-PY-009: Jinja2 autoescape disabled
env = Environment(autoescape=False)
template = env.from_string("<p>Hello {{ name }}</p>")
print(template.render(name="<script>alert('xss')</script>"))
