# FlaskCRUD_WebApp
A simple blogging web app that performs basic CRUD.

## I. Creating Virtual Environment
FOR WINDOWS:

`C:\Users\...\ProjectFolder>python -m venv venv`

FOR MacOS & LINUX:

`$ python -m venv venv`

## II. Activating Virtual Environment
FOR WINDOWS:

`C:\Users\...\ProjectFolder>venv\Scripts\activate`

FOR MacOS & LINUX:

`$ source venv\Scripts\activate`

## III. Deactivating Virtual Environment
FOR WINDOWS:

`C:\Users\...\ProjectFolder>deactivate`

FOR MacOS & LINUX:

`$ deactivate`

## IV. Installing multiple packages

`(venv) C:\Users\...\ProjectFolder>pip install -r requirements.txt`

## V. Generating database file
Be sure that your current working directory is the project folder
Go to Python shell and enter the following

`>>> from app import db`

`>>> db.create_all()`

`>>> exit()`
