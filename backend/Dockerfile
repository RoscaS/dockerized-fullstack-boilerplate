FROM python:3.8-rc-stretch

# Copy in your requirements file
ADD requirements.txt /requirements.txt

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN set -ex \
    && apt update && apt install -y build-essential \
            gcc \
            make \
            libc-dev \
            musl-dev \
            git \
    && pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip install --no-cache-dir -r requirements.txt"

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
ADD . /code/

RUN mkdir /logs/

# gunicorn will listen on this port
#EXPOSE 8000

# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=app.settings

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN DJANGO_SECRET_KEY=none python manage.py collectstatic --noinput

# Start gunicorn
ENTRYPOINT ["/code/entrypoint.sh"]
