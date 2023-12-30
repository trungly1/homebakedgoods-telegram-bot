# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for the database
# Replace 'your_password' with a secure password
ENV POSTGRES_DB=database
ENV POSTGRES_USER=daschronos
ENV POSTGRES_PASSWORD=Lightspeed123!

# Optional: Initialize the database with a script
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose the port the DB runs on
EXPOSE 5432
