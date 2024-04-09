# About the project

This is a simple diary in python that uses flask and sqlalchemy to do a page when you can write some things.

# Setup 

write in terminal:
```
pip install flask
pip install flask_sqlalchemy
```
After that, the project is ready to go but if you want to change something you must delete the instance folder then put your changes and write:
```
python
from main import app, db
app.app_context().push()
db.create_all()
```
It should create new instance and you have to repeat it every time you change something.
Thats it! Now run your program and type `127.0.0.1:5000` in your browser and it should work
