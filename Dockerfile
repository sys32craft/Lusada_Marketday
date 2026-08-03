FROM python:3.14.6-slim-trixie

ENV PYTHONUNBUFFERED=1

WORKDIR /project

# Install dependencies from the project root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

EXPOSE 8080

CMD ["python", "app/main.py"]