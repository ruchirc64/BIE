FROM python:3.9

# Install the Azure SDK
RUN pip install azure-storage-blob

# Copy your Streamlit app code into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Run Streamlit
CMD ["streamlit", "run", "main.py"]
