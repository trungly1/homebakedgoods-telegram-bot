# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for the database
# Replace 'your_password' with a secure password
ENV POSTGRES_DB=db_name
ENV POSTGRES_USER=db_user
ENV POSTGRES_PASSWORD=your_password

# Optional: Initialize the database with a script
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose the port the DB runs on
EXPOSE 5432
