# vnx-docker-007 eval target: missing HEALTHCHECK instruction
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# No HEALTHCHECK instruction present - TRIGGERS rule
CMD ["python", "app.py"]
