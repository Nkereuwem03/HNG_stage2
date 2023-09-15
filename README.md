# HNG_stage2

## Installation
Install Flask and Sqlalchemy using pip
```
pip install Flask 
pip install Flask-SQLAlchemy
```
Minimal Flask App 
```
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

if __name__ == '__main__': 
    app.run(port=5000)
```
Save this file as app.py (or any other filename you want) and go to the
terminal and type python app.py (i.e. python <filename>.py )
Launch any web browser and go to http://localhost:5000/hello/ to see the
app in action



### Basic UML Diagram

