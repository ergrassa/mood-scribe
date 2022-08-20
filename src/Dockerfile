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