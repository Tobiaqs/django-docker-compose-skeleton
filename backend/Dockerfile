FROM python:3.9 AS dev-backend
WORKDIR /app/
EXPOSE 8000
RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM dev-backend AS prod-backend
COPY . /app/
RUN python manage.py collectstatic
CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "--workers=2", "--threads=2", "--bind", "0.0.0.0:8000", "skeleton.wsgi:application"]
