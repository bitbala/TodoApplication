FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate


# Expose the port on which the Django app will run
EXPOSE 8080

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
