# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt wordnet stopwords

# Copy project files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Command to run the web app
CMD ["streamlit", "run", "webapp.py"]

