# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Run the scraper in the background and then start the Streamlit app
CMD ["sh", "-c", "python src\utils\scraper\scraper.py & streamlit run app.py --server.port 8501 --server.headless True"]
