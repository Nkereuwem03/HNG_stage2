# HNG_stage2

## Installation
Install Flask, Sqlalchemy and jsonschema using pip
```
pip install Flask 
pip install Flask-SQLAlchemy
pip install jsonschema

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
Launch any web browser and go to http://localhost:5000/ to see the
app in action

# Simple CRUD API
This is a sample API documentation for microservice. It is is to perform CRUD operations of a "person" resources.

## Version: 1.0.0
**Contact information:**  nkereuwem.udoudo1@gmail.com  

### /api
#### POST
##### Summary: Create person
##### Description: Endpoint to create person.
##### Endpoint
```
https://nkereuwem-flask-api.onrender.com/api
```
##### Sample request data: (as json object, "type"="string")
```
{"name": "nkereuwem udoudo"}
```
##### Sample Responses
| Code | Description |
| ---- | ----------- |
| 200 | successful operation |
| 500 | create error |

```
{'Message': 'Created Successfully'}
```

### /api/{user_id}
#### GET
##### Summary: Get user by person ID
##### Description: Endpoint to retrieve person
##### Parameters
| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | url path | The ID that needs to be fetched. e.g. (1)  | Yes | integer |
##### Endpoint
```
https://nkereuwem-flask-api.onrender.com/api/1
``` 
##### Responses
| Code | Description |
| ---- | ----------- |
| 200 | successful operation |
| 404 | Not found |

#### PUT
##### Summary: Update Person
##### Description: Endpoint to update person.
##### Parameters
| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path | ID that need to be deleted | Yes | integer |
##### Endpoint
```
https://nkereuwem-flask-api.onrender.com/api/1
``` 
##### Sample request data: (as json object, "type"="string")
```
{"name": "nkereuwem udoudo"}
```
##### Responses
| Code | Description |
| ---- | ----------- |
| 404 | Not found |
| 500 | error updating |
| 200 | operation successfull |

#### DELETE
##### Summary: Delete Person
##### Description: Endpoint to delete person.
##### Parameters
| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| user_id | path | The ID that needs to be deleted | Yes | integer |
##### Endpoint
```
https://nkereuwem-flask-api.onrender.com/api/1
``` 
##### Responses
| Code | Description |
| ---- | ----------- |
| 200 | delete successfull |
| 404 |not found |

### Basic UML Diagram
![Flask Rest API](https://github.com/Nkereuwem03/HNG_stage2/assets/105097028/8ddaf9ad-9f31-458a-b682-860bea1a6d7b)

### Basic E-R Diagram

![E-R diagram](https://github.com/Nkereuwem03/HNG_stage2/assets/105097028/92fc59c9-32dd-4ab4-81f1-7c1253113646)




