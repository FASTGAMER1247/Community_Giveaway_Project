import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'giveaway_project.settings'
django.setup()

from django.contrib.auth.models import User

# Let's use test client to generate session cookie for 'rahul_sharma'
from django.test import Client
client = Client()
logged_in = client.login(username='rahul_sharma', password='password123')
print("Client login successful:", logged_in)

session_key = client.session.session_key
print("Session key:", session_key)

with open("screenshots/session_cookie.txt", "w") as f:
    f.write(session_key)
