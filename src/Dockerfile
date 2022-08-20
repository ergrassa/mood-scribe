FROM python:slim
WORKDIR /app
EXPOSE 80
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN django-admin startproject mood
RUN cd mood && django-admin startapp scribe
COPY ./ ./mood/
RUN sed -i "s~___secretkey___~$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 128 | head -n 1)~" /app/mood/mood/settings.py