
Электронное меню ресторана

<!-- COPY: -->
git clone https://github.com/Damir-p/Electronic-menu-for-a-restaurant.git

<!-- VIRTUALENV -->
python3 -m venv venv

<!-- ACTIVATE VENV -->
source venv/bin/activate

<!-- MIGRATIONS -->
python manage.py migrate

<!-- RUN -->
python manage.py runserver 127.0.0.1:8000

<!-- DOCKER RUN  -->
docker-compose up