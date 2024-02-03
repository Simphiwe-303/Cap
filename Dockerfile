FROM pypy:latest
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python manage.py migrate
RUN python manage.py makemigrations fictional_bands
RUN python manage.py sqlmigrate fictional_bands 0001
RUN python manage.py migrate
CMD ["python", "manage.py", "createsuperuser"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
