ls -R /app
cd mood
python manage.py migrate
python manage.py runserver 0.0.0.0:80