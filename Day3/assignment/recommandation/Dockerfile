# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /recommandation

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Django default port
EXPOSE 8000

# Run the Django app
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
