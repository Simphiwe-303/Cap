FROM pypy:latest
WORKDIR /app
COPY . /app
RUN python -m pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py makemigrations fictional_bands
RUN python manage.py sqlmigrate fictional_bands 0001
RUN python manage.py migrate
CMD python manage.py runserver