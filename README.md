# job-backend

python3 -m venv .venv
source .venv/bin/activate
pip install flask
pip install Flask-RESTful
touch app.py
flask run

pip install Flask-SQLAlchemy
touch models.py
pip install flask-migrate
flask db init
flask db revision --autogenerate -m " "
flask db upgrade head
