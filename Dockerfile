# Download base image
FROM node:18

# Set working directory
WORKDIR ./cribl/assigment/

# Copy the rest of the application files
COPY ./cribl/assignment/ .