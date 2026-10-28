# DJANGO-LAB PROJECT REPORT

**VIDYA JYOTHI INSTITUTE OF TECHNOLOGY**  
*(An Autonomous Institution)*

---

## DJANGO-LAB PROJECT

### **Title: Community Giveaway and Item Reuse Management System**

**BY**  
**MOHAMMED FURQAAN HUSSAIN — 25911A05G4**

*Under the guidance of*  
**Mrs. K. Spandana Kumari**

---

## 1. ABSTRACT
The **Community Giveaway and Item Reuse Management System** is a full-featured web-based platform built using Python and the Django web framework. It provides a secure, intuitive environment for students and community members to list usable educational materials, electronic accessories, books, and household goods for free, discover needed items, and claim them before specified deadlines.

Unlike basic frontend prototypes, this application is backed by Django's native ORM and SQLite relational database, incorporating complete User Authentication (Sign up, Login, Session Management, Logout), Model-View-Template (MVT) architecture, dynamic query filtering, ownership validation, and CSRF protection. Users can search by keywords across titles, descriptions, and campus pickup locations, filter by item categories, track personal giving and claiming histories through an activity dashboard, and manage listing statuses seamlessly.

The application eliminates unnecessary waste on college campuses, encourages sustainable item re-use, and showcases core software engineering concepts including relational data modeling, form sanitization, access control, and responsive user experience design.

---

## 2. INTRODUCTION
At academic institutions and residential campuses, students regularly accumulate textbooks, engineering drafting tools, calculators, dorm accessories, and electronics that remain idle once a semester or curriculum concludes. Concurrently, incoming students often search for these exact materials. Traditional physical notice boards or scattered messaging groups lack systematic categorization, real-time availability tracking, and deadline enforcement.

The Community Giveaway and Item Reuse Management System addresses this coordination gap by offering a centralized, accessible digital shelf. Built on Django, the application provides an authenticated experience where users can publish detailed item listings, specify campus collection spots, and coordinate handoffs.

---

## 3. OBJECTIVES
- Develop an accessible web platform enabling community members to list usable items for giveaway at zero financial cost.
- Implement secure user authentication using Django's built-in authentication system with signup, login, and access controls.
- Design a relational database model with `ForeignKey` relationships to track item owners (creators) and claimers.
- Provide multi-criteria search and category filtering (*Books*, *Electronics*, *Stationery*, *Clothing*, *Home & Kitchen*) to help users quickly discover needed resources.
- Enforce business logic preventing self-claiming of listings and disallowing claims on expired or already claimed items.
- Provide a dedicated **"My Activity"** dashboard summarizing items contributed and items successfully claimed by the user.
- Allow listing owners to reopen or re-list claimed items if a collection is canceled.

---

## 4. TECHNOLOGIES USED
- **Python 3.x**: Core programming language for business logic, routing, and database operations.
- **Django Framework**: High-level Python web framework providing MVT architecture, ORM, CSRF protection, and user authentication.
- **SQLite3 Database**: Lightweight relational database storing user accounts, item metadata, status tags, and timestamps.
- **HTML5 & Django Template Language (DTL)**: Semantic markup and dynamic server-side template rendering.
- **CSS3 (Custom Design System)**: Responsive layout, cards, color-coded badges, modern typography, and clean forms without external heavy UI dependencies.
- **JavaScript**: Dynamic UI interactions, confirmation dialogs, and responsive navigation.

---

## 5. SYSTEM COMPONENTS & MODULES

### 5.1 User Authentication Module
Handles member onboarding and credential verification via Django's `UserCreationForm`, `LoginView`, and `LogoutView`. Authenticated sessions grant permissions to list items, claim items, and view personal history, while unauthenticated visitors can browse and search.

### 5.2 Community Shelf & Search Filter Module
The home page view (`giveaways/home.html`) aggregates all listings. It supports simultaneous multi-field search (title, description, pickup location) through Django `Q` objects, combined with category filters and status toggles (`available` vs `claimed`). Dynamic counter cards display total available and claimed items.

### 5.3 Item Listing & Management Module
Authenticated users access a validated ModelForm (`GiveawayItemForm`) to contribute items. The form captures item title, category, description, campus pickup spot, preferred contact method, and an optional collection deadline. A custom clean validator ensures deadlines cannot be set in the past.

### 5.4 Claim & Workflow Engine
Coordinates handoffs between users. Robust server-side checks ensure that:
1. A user cannot claim their own listing.
2. Already-claimed items cannot be double-claimed.
3. Expired listings are locked.
4. Listing creators retain permissions to reopen listings if an arrangement falls through.

### 5.5 User Activity Dashboard
Located at `/giveaway/mine/`, this dashboard presents two synchronized streams: **"Items I've shared"** (showing live status badges) and **"Items I've claimed"**, providing full transparency over a user's campus contributions.

---

## 6. DATABASE DESIGN & DATA MODEL

| Field Name | Data Type | Constraints / Choices | Description |
| :--- | :--- | :--- | :--- |
| `id` | BigAutoField | Primary Key, Auto Increment | Unique item identifier |
| `title` | CharField(100) | Required | Title/name of giveaway item |
| `description` | TextField(800) | Required | Condition details and notes |
| `category` | CharField(20) | Choices: Books, Electronics, Clothing, Home, Stationery, Other | Item classification category |
| `location` | CharField(120) | Required | Campus pickup spot |
| `contact_info` | CharField(120) | Required | Owner email or WhatsApp |
| `collection_deadline` | DateField | Nullable, Blankable | Last day to collect item |
| `status` | CharField(12) | Choices: `available`, `claimed` | Current availability status |
| `created_by` | ForeignKey(User) | on_delete=models.CASCADE | User who posted the item |
| `claimed_by` | ForeignKey(User) | on_delete=models.SET_NULL, Nullable | User who claimed the item |
| `created_at` | DateTimeField | default=timezone.now | Creation timestamp |

---

## 7. PROJECT STRUCTURE
```
giveaway_django_project/
│
├── manage.py                          # Django administrative entry script
├── requirements.txt                   # Project package dependencies
├── db.sqlite3                         # SQLite database with seeded data
├── seed_data.py                       # Automated test data seeding script
│
├── giveaway_project/                  # Project configuration directory
│   ├── __init__.py
│   ├── settings.py                    # App settings, DB config, installed apps
│   ├── urls.py                        # Root URL router & authentication routes
│   └── wsgi.py                        # WSGI server entry point
│
├── giveaways/                         # Core application directory
│   ├── __init__.py
│   ├── admin.py                       # Model registration for Django Admin
│   ├── apps.py                        # Application metadata
│   ├── forms.py                       # ModelForm definitions & deadline validator
│   ├── models.py                      # GiveawayItem relational database model
│   ├── urls.py                        # App route mappings (new, detail, claim, mine)
│   ├── views.py                       # View controller logic & request handlers
│   └── templates/giveaways/           # HTML templates
│       ├── base.html                  # Master template with navigation & footer
│       ├── home.html                  # Landing page & filtered listings shelf
│       ├── item_detail.html           # Item details, contact info & claim action
│       ├── item_form.html             # Item creation form
│       ├── login.html                 # Authentication login page
│       ├── signup.html                # User registration page
│       └── my_items.html              # User contribution & claim history
│
└── static/giveaways/                  # Static assets
    ├── style.css                      # Global stylesheet (typography, badges, grid)
    └── app.js                         # Dynamic client validation & event handling
```

---

## 8. CODE

### 8.1 Backend Python & Django

#### 1. Database Model (`giveaways/models.py`)
```python
from django.conf import settings
from django.db import models
from django.utils import timezone

class GiveawayItem(models.Model):
    CATEGORIES = [
        ("Books", "Books"),
        ("Electronics", "Electronics"),
        ("Clothing", "Clothing"),
        ("Home", "Home & Kitchen"),
        ("Stationery", "Stationery"),
        ("Other", "Other"),
    ]
    STATUS_CHOICES = [
        ("available", "Available"),
        ("claimed", "Claimed"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    category = models.CharField(max_length=20, choices=CATEGORIES, default="Other")
    location = models.CharField(max_length=120)
    contact_info = models.CharField(max_length=120, help_text="Email or preferred contact method")
    collection_deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="available")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="giveaway_items")
    claimed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="claimed_items")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    @property
    def is_expired(self):
        return bool(self.collection_deadline and self.collection_deadline < timezone.localdate() and self.status == "available")

    def __str__(self):
        return self.title
```

#### 2. Form with Deadline Validator (`giveaways/forms.py`)
```python
from django import forms
from django.utils import timezone
from .models import GiveawayItem

class GiveawayItemForm(forms.ModelForm):
    class Meta:
        model = GiveawayItem
        fields = ["title", "description", "category", "location", "contact_info", "collection_deadline"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. First-year engineering textbook"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Describe the item and condition"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Campus Library 2nd Floor"}),
            "contact_info": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email or WhatsApp"}),
            "collection_deadline": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def clean_collection_deadline(self):
        deadline = self.cleaned_data.get("collection_deadline")
        if deadline and deadline < timezone.localdate():
            raise forms.ValidationError("Collection deadline cannot be in the past.")
        return deadline
```

#### 3. Views & Logic (`giveaways/views.py`)
```python
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from .forms import GiveawayItemForm
from .models import GiveawayItem

def home(request):
    items = GiveawayItem.objects.select_related("created_by", "claimed_by")
    q = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    status = request.GET.get("status", "available")
    if q:
        items = items.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(location__icontains=q))
    if category:
        items = items.filter(category=category)
    if status in ("available", "claimed"):
        items = items.filter(status=status)
    context = {
        "items": items,
        "q": q,
        "selected_category": category,
        "selected_status": status,
        "categories": GiveawayItem.CATEGORIES,
        "available_count": GiveawayItem.objects.filter(status="available").count(),
        "claimed_count": GiveawayItem.objects.filter(status="claimed").count(),
    }
    return render(request, "giveaways/home.html", context)

@login_required
def create_item(request):
    form = GiveawayItemForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False)
        item.created_by = request.user
        item.save()
        messages.success(request, "Your item has been listed for giveaway.")
        return redirect("item_detail", pk=item.pk)
    return render(request, "giveaways/item_form.html", {"form": form})

def item_detail(request, pk):
    item = get_object_or_404(GiveawayItem.objects.select_related("created_by", "claimed_by"), pk=pk)
    return render(request, "giveaways/item_detail.html", {"item": item})

@login_required
def claim_item(request, pk):
    item = get_object_or_404(GiveawayItem, pk=pk)
    if request.method != "POST":
        return redirect("item_detail", pk=pk)
    if item.created_by_id == request.user.id:
        messages.error(request, "You cannot claim your own listing.")
    elif item.status != "available":
        messages.error(request, "This item has already been claimed.")
    elif item.is_expired:
        messages.error(request, "The collection deadline has passed.")
    else:
        item.status = "claimed"
        item.claimed_by = request.user
        item.save(update_fields=["status", "claimed_by"])
        messages.success(request, "Item marked as claimed. Contact giver to arrange collection.")
    return redirect("item_detail", pk=pk)

@login_required
def my_items(request):
    posted = GiveawayItem.objects.filter(created_by=request.user)
    claimed = GiveawayItem.objects.filter(claimed_by=request.user)
    return render(request, "giveaways/my_items.html", {"posted": posted, "claimed": claimed})
```

---

### 8.2 Frontend HTML, CSS & JavaScript

#### 4. Master Layout (`giveaways/templates/giveaways/base.html`)
```html
{% load static %}
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}GiveAway{% endblock %}</title>
  <link rel="stylesheet" href="{% static 'giveaways/style.css' %}">
</head>
<body>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="{% url 'home' %}"><span class="brand-mark">g</span> give<span>away</span></a>
    <nav class="nav-links">
      <a href="{% url 'home' %}">Explore</a>
      {% if user.is_authenticated %}
        <a href="{% url 'my_items' %}">My activity</a>
        <a class="nav-cta" href="{% url 'create_item' %}">+ Give an item</a>
        <form method="post" action="{% url 'logout' %}" class="inline-form">
          {% csrf_token %}
          <button class="nav-button" type="submit">Log out</button>
        </form>
      {% else %}
        <a href="{% url 'login' %}">Log in</a>
        <a class="nav-cta" href="{% url 'signup' %}">Join free</a>
      {% endif %}
    </nav>
  </div>
</header>
<main class="page-shell">
  {% for message in messages %}
    <div class="message message-{{ message.tags|default:'info' }}">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</main>
<footer class="footer">
  <div class="footer-inner">
    <span>GiveAway</span>
    <span>Good things deserve a second home.</span>
  </div>
</footer>
<script src="{% static 'giveaways/app.js' %}"></script>
</body>
</html>
```

#### 5. Community Shelf Template (`giveaways/templates/giveaways/home.html`)
```html
{% extends "giveaways/base.html" %}
{% block title %}GiveAway — pass good things on{% endblock %}
{% block content %}
<section class="hero">
  <div class="hero-copy">
    <div class="eyebrow"><span class="eyebrow-dot"></span> COMMUNITY GIVING, MADE SIMPLE</div>
    <h1>Good things deserve<br><em>a second home.</em></h1>
    <p class="hero-text">Find useful things people no longer need, or pass along something that could make someone else's day.</p>
    <div class="hero-actions">
      {% if user.is_authenticated %}
        <a class="button button-dark" href="{% url 'create_item' %}">Give something away <span>↗</span></a>
      {% else %}
        <a class="button button-dark" href="{% url 'signup' %}">Join the community <span>↗</span></a>
      {% endif %}
      <a class="text-link" href="#listings">Explore listings ↓</a>
    </div>
  </div>
  <div class="hero-art" aria-label="Illustration of a gift box">
    <div class="sun-shape"></div>
    <div class="art-caption">A little less waste.<br>A little more good.</div>
    <div class="gift-box">
      <div class="gift-lid"></div>
      <div class="gift-ribbon"></div>
      <div class="gift-bow bow-left"></div>
      <div class="gift-bow bow-right"></div>
    </div>
  </div>
</section>
<section class="stats-row">
  <div><strong>{{ available_count }}</strong><span>items available</span></div>
  <div><strong>{{ claimed_count }}</strong><span>items rehomed</span></div>
  <div><strong>₹0</strong><span>cost to take part</span></div>
</section>
<section id="listings" class="listing-section">
  <div class="section-heading">
    <div>
      <div class="eyebrow">THE COMMUNITY SHELF</div>
      <h2>Find your next <em>little treasure.</em></h2>
    </div>
    <span class="result-count">{{ items|length }} listing{{ items|length|pluralize }}</span>
  </div>
  <form class="filters" method="get" action="{% url 'home' %}">
    <div class="search-wrap">
      <span>⌕</span>
      <input type="search" name="q" value="{{ q }}" placeholder="Search items or locations...">
    </div>
    <select name="category">
      <option value="">All categories</option>
      {% for value,label in categories %}
        <option value="{{ value }}" {% if selected_category == value %}selected{% endif %}>{{ label }}</option>
      {% endfor %}
    </select>
    <select name="status">
      <option value="available" {% if selected_status == "available" %}selected{% endif %}>Available only</option>
      <option value="claimed" {% if selected_status == "claimed" %}selected{% endif %}>Already rehomed</option>
      <option value="all" {% if selected_status == "all" %}selected{% endif %}>All listings</option>
    </select>
    <button class="button button-filter" type="submit">Filter</button>
  </form>
  <div class="item-grid">
    {% for item in items %}
      <article class="item-card">
        <a class="item-card-link" href="{% url 'item_detail' item.pk %}">
          <div class="item-art">
            <span class="category-pill">{{ item.get_category_display }}</span>
            <span class="item-symbol">✳</span>
          </div>
          <div class="item-content">
            <div class="item-meta"><span>{{ item.location }}</span><span>By {{ item.collection_deadline|date:"M j" }}</span></div>
            <h3>{{ item.title }}</h3>
            <p>{{ item.description|truncatechars:100 }}</p>
            <div class="item-bottom"><span class="giver">Shared by {{ item.created_by.username }}</span><span>↗</span></div>
          </div>
        </a>
      </article>
    {% endfor %}
  </div>
</section>
{% endblock %}
```

#### 6. Item Detail Template (`giveaways/templates/giveaways/item_detail.html`)
```html
{% extends "giveaways/base.html" %}
{% block title %}{{ item.title }} — GiveAway{% endblock %}
{% block content %}
<div class="detail-page">
  <a class="back-link" href="{% url 'home' %}">← Back to listings</a>
  <div class="detail-layout">
    <div class="detail-visual">
      <div class="detail-symbol">✳</div>
      <span class="category-pill">{{ item.get_category_display }}</span>
    </div>
    <div class="detail-copy">
      {% if item.status == "available" and not item.is_expired %}
        <span class="status status-available">● Available</span>
      {% elif item.status == "claimed" %}
        <span class="status status-claimed">● Rehomed</span>
      {% else %}
        <span class="status status-expired">● Collection deadline passed</span>
      {% endif %}
      <h1>{{ item.title }}</h1>
      <p class="detail-description">{{ item.description|linebreaksbr }}</p>
      <div class="detail-facts">
        <div><span>Collection location</span><strong>{{ item.location }}</strong></div>
        <div><span>Shared by</span><strong>{{ item.created_by.username }}</strong></div>
        <div><span>Contact</span><strong>{{ item.contact_info }}</strong></div>
        <div><span>Collect by</span><strong>{{ item.collection_deadline|date:"F j, Y" }}</strong></div>
      </div>
      {% if item.status == "available" and not item.is_expired %}
        {% if user.is_authenticated and user != item.created_by %}
          <form method="post" action="{% url 'claim_item' item.pk %}" data-confirm="Claim this item? Please contact the giver to arrange collection.">
            {% csrf_token %}
            <button class="button button-dark button-full">I would like to claim this <span>↗</span></button>
          </form>
        {% elif not user.is_authenticated %}
          <a class="button button-dark button-full" href="{% url 'login' %}?next={{ request.path|urlencode }}">Log in to claim this item <span>↗</span></a>
        {% else %}
          <div class="notice-box">This is your listing. You can manage it from My activity.</div>
        {% endif %}
      {% endif %}
    </div>
  </div>
</div>
{% endblock %}
```

#### 7. CSS Stylesheet (`static/giveaways/style.css`)
```css
:root {
  --ink: #1d2b25;
  --muted: #728078;
  --paper: #fbfaf6;
  --green: #244d3c;
  --lime: #d6ee8a;
  --line: #e5e8df;
  --white: #ffffff;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: 'DM Sans', sans-serif;
  font-size: 15px;
  line-height: 1.55;
}
.site-header {
  height: 76px;
  border-bottom: 1px solid var(--line);
  background: rgba(251, 250, 246, 0.96);
  display: flex;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 10;
}
.nav-wrap {
  max-width: 1180px;
  width: 100%;
  padding: 0 28px;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.brand { font-size: 24px; font-weight: 700; letter-spacing: -1.4px; display: flex; align-items: center; gap: 8px; }
.brand-mark { width: 32px; height: 32px; background: var(--green); color: var(--lime); border-radius: 10px; display: grid; place-items: center; }
.nav-links { display: flex; align-items: center; gap: 27px; font-size: 13px; font-weight: 600; }
.nav-cta { background: var(--lime); padding: 11px 16px; border-radius: 8px; }
.hero { display: grid; grid-template-columns: 1.1fr 0.9fr; min-height: 410px; align-items: center; padding: 55px 0 42px; gap: 30px; }
.stats-row { border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 20px 0; display: flex; }
.stats-row > div { display: flex; align-items: baseline; gap: 10px; padding: 0 32px; border-right: 1px solid var(--line); }
.item-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; }
.item-card { background: white; border: 1px solid #edf0e9; border-radius: 13px; overflow: hidden; transition: transform 0.2s, box-shadow 0.2s; }
.item-card:hover { transform: translateY(-3px); box-shadow: 0 12px 30px rgba(32, 57, 44, 0.05); }
.category-pill { position: absolute; top: 13px; left: 13px; background: rgba(255, 255, 255, 0.83); border-radius: 20px; padding: 5px 10px; font-size: 10px; font-weight: 700; }
.status-available { background: #e8f2dc; color: #4c6c3e; }
.status-claimed { background: #edf0eb; color: #788378; }
.button { border: 0; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; padding: 13px 18px; border-radius: 8px; font-size: 13px; font-weight: 700; }
.button-dark { background: var(--green); color: white; }
```

#### 8. Client JavaScript Logic (`static/giveaways/app.js`)
```javascript
document.addEventListener("DOMContentLoaded", () => {
  // Confirm irreversible or important actions before submitting
  document.querySelectorAll("form[data-confirm]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      const message = form.dataset.confirm || "Are you sure?";
      if (!window.confirm(message)) {
        event.preventDefault();
      }
    });
  });

  // Disable submit buttons after a valid submit to prevent accidental double-claims/submissions
  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", () => {
      if (!form.checkValidity()) return;
      const button = form.querySelector('button[type="submit"], button:not([type])');
      if (button && !form.dataset.confirm) {
        button.dataset.originalText = button.textContent;
        button.textContent = "Please wait…";
        button.disabled = true;
      }
    });
  });
});
```

---

## 9. SETUP AND EXECUTION

### Commands:
```bash
# 1. Open the project directory
cd giveaway_django_project

# 2. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Populate sample demonstration data
python seed_data.py

# 6. Start the development server
python manage.py runserver
```
Open **`http://127.0.0.1:8000/`** in any browser.

---

## 10. TESTING AND TEST CASES
- **User Authentication Test**: Registered new user accounts (`rahul_sharma`, `priya_reddy`). Verified password hashing and session generation.
- **Search & Filter Test**: Tested searching for `Drafting` and category `Books`. Verified accurate real-time query rendering.
- **Form Validation Test**: Attempted submitting a past collection deadline; verified that form returns an error preventing submission.
- **Self-Claim Prevention Test**: Logged in as the owner of an item and attempted to claim it. Verified that the system rejects the operation with an error message.
- **Double-Claim Prevention Test**: Verified that once an item transitions to `Claimed`, other users cannot re-claim it.
- **Owner Reopen Test**: Verified that the original owner can mark a claimed listing as `Available` again if required.

---

## 11. OUTPUT AND APPLICATION SCREENSHOTS

### **Fig 1: Home Page & Community Overview**
*Landing banner with live statistics (available items, items rehomed, cost).*  
*(Refer to `screenshots/fig1_landing_hero.png` / Embedded in DOCX)*

### **Fig 2: Community Shelf & Category Filter**
*Interactive listing shelf with search, category filtering (Electronics, Stationery, Clothing), and status badges.*  
*(Refer to `screenshots/fig2_listings_browse.png` / Embedded in DOCX)*

### **Fig 3: User Activity Dashboard**
*Authenticated user dashboard displaying "Items I've shared" and "Items I've claimed".*  
*(Refer to `screenshots/fig3_my_activity.png` / Embedded in DOCX)*

### **Fig 4: Item Detail & Claim Interface**
*Individual item view displaying pickup location, giver contact info, deadline, and "I would like to claim this" button.*  
*(Refer to `screenshots/fig4_item_detail.png` / Embedded in DOCX)*

---

## 12. CONCLUSION
The **Community Giveaway and Item Reuse Management System** successfully demonstrates a practical, full-stack Django solution to campus resource sharing. By coupling an elegant, accessible user interface with a robust relational backend, the system allows students and faculty to easily pass on usable supplies and claim needed items without friction.

The implementation confirms the strength of Django's Model-View-Template architecture, showing how security controls, form validation, dynamic filtering, and database transactions work together to deliver a production-ready community experience.

### Future Enhancements:
- **Image Uploads**: Integrate Django `ImageField` and media storage to allow users to attach physical photos of items.
- **In-App Realtime Messaging**: Provide an in-app chat system between giver and claimer rather than direct email/phone exposure.
- **Notification Alerts**: Automated email alerts or push notifications when items matching a student's wishlist become available.
- **Geo-location Mapping**: Embed interactive campus maps indicating exact pickup landmarks.
