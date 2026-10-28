# GiveAway — Django mini project

A small community web app where users can list usable items for free, browse listings, and claim items they need.

## Stack
- Python + Django
- SQLite database
- Django authentication
- HTML templates, custom CSS, and JavaScript
- No paid API or separate database server required

## Windows setup (VS Code terminal)
Extract the ZIP, open the `giveaway_django` folder in VS Code, then run:

```bat
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Open http://127.0.0.1:8000/

Create a normal user account using **Join free**. The superuser is useful for the admin page at http://127.0.0.1:8000/admin/.

## macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Features
- Signup, login, logout
- List items for free with category, location, contact details, and collection deadline
- Browse, search, and filter by category/status
- Claim an available item (only logged-in users; cannot claim own item)
- Listing owner can reopen a claimed listing
- My Activity page showing posted and claimed items
- Deadline validation and expired-listing handling
- Django admin

## Notes
- The listing's contact information is visible on the item detail page. Use demo contact details during a lab demonstration.
- The project is intended for local educational use. Before deployment, replace the development secret key, set `DEBUG=False`, configure `ALLOWED_HOSTS`, and review security settings.
- Bootstrap is not required; styling is custom CSS. Google Fonts are optional and loaded remotely.
