# Weavers Group AI lab Coding Assignment
This FastAPI-based application provides a RESTful API to manage prompts.  
It includes the following features:

- Ability to view, add, edit, and delete prompts  
- Ability to leave a change message when editing a prompt  
- Ability to view the history of changes for each prompt  

## Requirements
- Python 3.12+
- PostgreSQL 17
- Virtual environment (recommended)

## Instructions
 - git clone https://github.com/RyanAOGallagher/weavers-coding-assignment.git
 - cd weavers-coding-assignment
 - python -m venv venv
 - pip install FastAPI[all] SQLAlchemy psycopg2-binary uvicorn
 - Open pgadmin and create new database 
   - name: weaversdb
   - password: password
 - run uvicorn main:app --reload
 

## API Endpoints

| Method  | Endpoint                        | Description                               | Request Body |
|---------|---------------------------------|-------------------------------------------|--------------|
| `GET`   | `/prompts/`                     | Get all prompts                          | *None*       |
| `GET`   | `/prompts/{prompt_id}/`         | Get a single prompt                      | *None*       |
| `POST`  | `/prompts/`                     | Create a new prompt                      | `{ "text": "string" }` |
| `PUT`   | `/prompts/{prompt_id}/`         | Update a prompt with a change message    | `{ "text": "string", "change_message": "string" }` |
| `DELETE`| `/prompts/{prompt_id}/`         | Delete a prompt                          | *None*       |
| `GET`   | `/prompts/{prompt_id}/history`  | Get prompt change history                | *None*       |

