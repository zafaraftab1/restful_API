# practice_rest_api

A small Django REST API project created for practice.

Contents
- Django project: `practice_rest_api`
- App: `restfull_api`
- Database: SQLite (db.sqlite3)

Prerequisites
- Python 3.10+ (project appears to use Python 3.12 artifacts but 3.10+ should work)
- pip
- (Optional) virtualenv or venv

Setup (macOS / Linux)

1. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirment.txt
```

3. Apply migrations

```bash
python manage.py migrate
```

4. Create a superuser (optional, for admin)

```bash
python manage.py createsuperuser
```

5. Run the development server

```bash
python manage.py runserver
```

Project notes
- The project uses a custom user model: `AUTH_USER_MODEL = 'restfull_api.UserProfile'` (see `practice_rest_api/settings.py`).
- The repo includes `rest_framework` and `rest_framework.authtoken` in `INSTALLED_APPS`.
- If you add or change REST framework settings, check `practice_rest_api/settings.py` for duplicate or overwritten `REST_FRAMEWORK` variables.

How to explore the API
- Start the server and open `http://127.0.0.1:8000/`.
- Visit Django admin at `http://127.0.0.1:8000/admin/` (requires superuser).
- The API routes are defined in the app `restfull_api` — consult `restfull_api/urls.py` for the exact endpoints.

Troubleshooting
- If you see issues importing modules, ensure your virtual environment is active and dependencies are installed.
- If the database schema is out of sync, run `python manage.py makemigrations` and `python manage.py migrate`.

License
- This README and the supplied project files have no license specified. Add a `LICENSE` file if you intend to open-source this project.

