### How to run the aruppi project?

1. Clone the repository in your desktop.
```[bash]
https://github.com/xsarias/AruppiProject.git
```
2. Create the database in your localhost, and configure Environment Variables.
3. Create the virtual environment in Aruppi folder.
```[bash]
virtualenv env
```
4. Activate virtualenv.
```[bash]
source env/scripts/activate
```

5. Install poetry and requirements.txt
```[bash]
pip install poetry
poetry install
pip install -r requirements.txt
```

6. Run uvicorn for FastAPI services.
```[bash]
uvicorn aruppi_project.main:app --reload
```

7. Go to the localhost and try the services.