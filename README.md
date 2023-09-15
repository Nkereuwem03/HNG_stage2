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

Save this file as app.py (or any other filename you want) and go to the
terminal and type python app.py (i.e. python <filename>.py )
Launch any web browser and go to http://localhost:5000/hello/ to see the
app in action

# Simple CRUD API
This is a sample API documentation for microservice

## Version: 1.0.0
### Terms of service
http://swagger.io/terms/

**Contact information:**  
nkereuwem.udoudo1@gmail.com  
[Find out more about Swagger](null)

### /api
#### POST
##### Summary: Create person
##### Description: Endpoint to create person.
##### Responses
| Code | Description |
| ---- | ----------- |
| default | successful operation |

### /api/{user_id}
#### GET
##### Summary: Get user by person ID
##### Description: Endpoint to retrieve person
##### Parameters
| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path | The ID that needs to be fetched. 1.  | Yes | integer |
##### Responses
| Code | Description |
| ---- | ----------- |
| 200 | successful operation |
| 404 | Person not found |

#### PUT
##### Summary: Update Person
##### Description: Endpoint to update person.
##### Parameters
| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path | ID that need to be deleted | Yes | integer |
##### Responses
| Code | Description |
| ---- | ----------- |
| 404 | person not found |
| 500 | error updating person |
| default | person created successfully |

#### DELETE
##### Summary: Delete Person
##### Description: Endpoint to delete person.
##### Parameters
| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path | The ID that needs to be deleted | Yes | integer |
##### Responses
| Code | Description |
| ---- | ----------- |
| 200 | person deleted successfully |
| 404 | person not found |

### Basic UML Diagram

