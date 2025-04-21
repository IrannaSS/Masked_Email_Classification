FROM python:3.9-slim

# Set environment variables to avoid interactive prompts
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /app

# Copy requirement files and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files
COPY . .

# Streamlit-specific configs to prevent browser opening
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose the default Streamlit port
EXPOSE 7860

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]