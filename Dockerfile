FROM python:3.11

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (HuggingFace uses 7860)
EXPOSE 7860

# Run your API
CMD ["uvicorn", "openenv.fast:app", "--host", "0.0.0.0", "--port", "7860"]
