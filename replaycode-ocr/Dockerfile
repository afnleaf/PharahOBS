FROM python:latest

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libopencv-dev \
    tesseract-ocr

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

CMD [ "python", "./src/main.py" ]
#CMD [ "python", "./src/ocr.py" ]
#CMD [ "python", "./src/test.py" ]

