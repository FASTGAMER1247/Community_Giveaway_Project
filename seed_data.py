import os
import django
from datetime import timedelta

os.environ['DJANGO_SETTINGS_MODULE'] = 'giveaway_project.settings'
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from giveaways.models import GiveawayItem

# Create or get users
users_data = [
    {"username": "rahul_sharma", "email": "rahul.sharma@example.com", "first_name": "Rahul", "last_name": "Sharma"},
    {"username": "priya_reddy", "email": "priya.reddy@example.com", "first_name": "Priya", "last_name": "Reddy"},
    {"username": "sneha_patel", "email": "sneha.patel@example.com", "first_name": "Sneha", "last_name": "Patel"},
    {"username": "arjun_verma", "email": "arjun.verma@example.com", "first_name": "Arjun", "last_name": "Verma"},
]

users = {}
admin_user = User.objects.first()
users["super"] = admin_user

for u in users_data:
    user, created = User.objects.get_or_create(username=u["username"], defaults={
        "email": u["email"],
        "first_name": u["first_name"],
        "last_name": u["last_name"]
    })
    if created:
        user.set_password("password123")
        user.save()
    users[u["username"]] = user

today = timezone.localdate()

sample_items = [
    {
        "title": "Engineering Mathematics - III (B.S. Grewal)",
        "description": "Hardcover textbook in great condition. Minimal pencil markings, all pages intact. Great for 2nd year students.",
        "category": "Books",
        "location": "Library Block, 2nd Floor, Campus",
        "contact_info": "rahul.sharma@example.com / WhatsApp: 9876543210",
        "collection_deadline": today + timedelta(days=7),
        "status": "available",
        "created_by": users["rahul_sharma"],
        "claimed_by": None,
    },
    {
        "title": "Logitech Wireless Mouse M185",
        "description": "Smooth working condition, comes with USB nano receiver and a fresh AA battery. Selling because I upgraded.",
        "category": "Electronics",
        "location": "Hostel Block B, Room 204",
        "contact_info": "priya.reddy@example.com",
        "collection_deadline": today + timedelta(days=5),
        "status": "available",
        "created_by": users["priya_reddy"],
        "claimed_by": None,
    },
    {
        "title": "Scientific Calculator (Casio fx-991EX)",
        "description": "Original Casio classwiz scientific calculator. Essential for engineering math and physics practicals.",
        "category": "Stationery",
        "location": "ECE Department Notice Board, Main Campus",
        "contact_info": "sneha.patel@example.com",
        "collection_deadline": today + timedelta(days=4),
        "status": "claimed",
        "created_by": users["sneha_patel"],
        "claimed_by": users["rahul_sharma"],
    },
    {
        "title": "Desk Study Lamp (Warm White LED)",
        "description": "Adjustable neck desk lamp with 3 brightness modes. USB powered, perfect for late night study sessions.",
        "category": "Home",
        "location": "Student Activity Center (SAC)",
        "contact_info": "arjun.verma@example.com",
        "collection_deadline": today + timedelta(days=10),
        "status": "available",
        "created_by": users["arjun_verma"],
        "claimed_by": None,
    },
    {
        "title": "Campus Sports Hoodie (Size L - Navy Blue)",
        "description": "Clean, gently used warm fleece college hoodie. Freshly washed, no tears or defects.",
        "category": "Clothing",
        "location": "Sports Complex / Gymnasium Entrance",
        "contact_info": "priya.reddy@example.com",
        "collection_deadline": today + timedelta(days=3),
        "status": "available",
        "created_by": users["priya_reddy"],
        "claimed_by": None,
    },
    {
        "title": "Drafting Kit & Engineering Drawing Board",
        "description": "Includes mini drafter, T-square, clips, and set squares for engineering graphics lab. Very clean.",
        "category": "Stationery",
        "location": "Mechanical Dept Workshop",
        "contact_info": "rahul.sharma@example.com",
        "collection_deadline": today + timedelta(days=8),
        "status": "available",
        "created_by": users["rahul_sharma"],
        "claimed_by": None,
    },
    {
        "title": "Data Structures & Algorithms in C++ by Mark Allen Weiss",
        "description": "Standard reference textbook for CSE / IT students. Very helpful for technical interview prep.",
        "category": "Books",
        "location": "CSE Lab 3",
        "contact_info": "super_admin@campus.edu",
        "collection_deadline": today + timedelta(days=12),
        "status": "claimed",
        "created_by": users["super"],
        "claimed_by": users["priya_reddy"],
    },
    {
        "title": "Noise Cancelling Wired Headset with Mic",
        "description": "3.5mm audio jack headset. Clear microphone sound, comfortable ear pads for online webinars and classes.",
        "category": "Electronics",
        "location": "Cafeteria Ground Floor",
        "contact_info": "sneha.patel@example.com",
        "collection_deadline": today + timedelta(days=6),
        "status": "available",
        "created_by": users["sneha_patel"],
        "claimed_by": None,
    }
]

created_count = 0
for item_data in sample_items:
    item, created = GiveawayItem.objects.get_or_create(
        title=item_data["title"],
        defaults=item_data
    )
    if created:
        created_count += 1

print(f"Successfully populated database! Added {created_count} new sample giveaway items.")
print(f"Total items in database: {GiveawayItem.objects.count()}")
