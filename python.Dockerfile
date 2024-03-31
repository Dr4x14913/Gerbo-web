FROM python:latest

# Install dependencies
RUN pip install dash mysql-connector-python flask pandas gunicorn dash-bootstrap-components gunicorn

# Copy local code to the container image.
COPY ./app /app

# Define working directory in the container
WORKDIR /app

# Expose port 8050 for the application
EXPOSE 8050

# Run app with gunicorn, assuming your python file is named "app.py" and it's located at "/app"
CMD ["gunicorn", "wsgi:application", "-b", ":8050", "-w", "6"]
