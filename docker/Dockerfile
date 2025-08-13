# Use official Python slim image
FROM python:3.13-alpine
# Set working directory
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all Python files
COPY *.py ./
COPY es.txt ./
#make main.py the main file and executable
RUN chmod +x main.py
# Set entrypoint
ENTRYPOINT ["python", "main.py"]