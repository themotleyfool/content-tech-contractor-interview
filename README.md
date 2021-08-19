# content-tech-contractor-interview

Project for Content Tech Contractor Interviews.

## Configure the Application

Run the following commands once to configure the application

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata datadump.json
```

## Run the Server

```bash
python manage.py runserver
```

## Website

<http://127.0.0.1:8000>

## Admin

Admin: <http://127.0.0.1:8000/admin>

### Admin Credentials

**Username:** admin  
**Password:** admin

## Acknowledgements

This project borrows liberally from the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/)
