FROM python:3.9
RUN pip install --upgrade pip
WORKDIR /tmp/
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
