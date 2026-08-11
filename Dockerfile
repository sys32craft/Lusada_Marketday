FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=120

WORKDIR /project

# Install dependencies first so Docker can cache this layer
COPY requirements.txt .

RUN pip install --no-cache-dir \
    --timeout 120 \
    --retries 10 \
    -r requirements.txt

# Copy application
COPY . .

# NiceGUI
EXPOSE 8080

# API
EXPOSE 5000

# Start API and NiceGUI
CMD ["sh", "-c", "python app/api.py & python app/main.py"]