# Use a stable version of Python
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

COPY . .

RUN pip install pandas
RUN pip install numpy
RUN pip install matplotlib

# Run your script
CMD ["python", "dataclean.py"]