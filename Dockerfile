FROM python:3.9

ENV PATH="/scripts:${PATH}"
ENV LIBRARY_PATH=/lib:/usr/lib

ENV PYTHONUNBUFFERED 1
RUN mkdir /musicplayer
WORKDIR /musicplayer
COPY . /musicplayer
ADD requirements/requirements.txt /musicplayer
RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate
RUN python manage.py makemigrations player
RUN python manage.py migrate player

CMD ["gunicorn", "--chdir", "musicplayer", "--bind", ":8001", "musicplayer.wsgi:application"]

EXPOSE 8001