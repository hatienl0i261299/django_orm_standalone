Run
```
docker-compose up --build -d
python manage.py makemigrations db
python manage.py migrate db
python main.py
```