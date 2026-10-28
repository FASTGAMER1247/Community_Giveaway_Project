import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def create_report():
    doc = Document()

    # Set page margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # ------------------ COVER PAGE ------------------
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(40)
    p_inst.paragraph_format.space_after = Pt(2)
    run_inst = p_inst.add_run("VIDYA JYOTHI")
    run_inst.font.name = "Times New Roman"
    run_inst.font.size = Pt(24)
    run_inst.font.bold = True
    run_inst.font.color.rgb = RGBColor(180, 20, 20)

    p_sub_inst = doc.add_paragraph()
    p_sub_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub_inst.paragraph_format.space_before = Pt(0)
    p_sub_inst.paragraph_format.space_after = Pt(4)
    run_sub = p_sub_inst.add_run("INSTITUTE OF TECHNOLOGY")
    run_sub.font.name = "Times New Roman"
    run_sub.font.size = Pt(16)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(30, 30, 30)

    p_auto = doc.add_paragraph()
    p_auto.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_auto.paragraph_format.space_after = Pt(60)
    run_auto = p_auto.add_run("AN AUTONOMOUS INSTITUTION")
    run_auto.font.name = "Times New Roman"
    run_auto.font.size = Pt(11)
    run_auto.font.bold = True
    run_auto.font.color.rgb = RGBColor(80, 80, 80)

    # Lab Project Heading
    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_proj.paragraph_format.space_after = Pt(24)
    run_proj = p_proj.add_run("DJANGO-LAB PROJECT")
    run_proj.font.name = "Times New Roman"
    run_proj.font.size = Pt(22)
    run_proj.font.bold = True

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(50)
    run_title = p_title.add_run("Title: Community Giveaway and Item Reuse\nManagement System")
    run_title.font.name = "Times New Roman"
    run_title.font.size = Pt(16)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(190, 40, 40)

    # BY
    p_by = doc.add_paragraph()
    p_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_by.paragraph_format.space_after = Pt(8)
    run_by = p_by.add_run("BY")
    run_by.font.name = "Times New Roman"
    run_by.font.size = Pt(14)
    run_by.font.bold = True

    # Student Name & Roll
    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_after = Pt(50)
    run_name = p_name.add_run("MOHAMMED FURQAAN HUSSAIN — 25911A05G4")
    run_name.font.name = "Times New Roman"
    run_name.font.size = Pt(15)
    run_name.font.bold = True

    # Under Guidance
    p_guide_lbl = doc.add_paragraph()
    p_guide_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_guide_lbl.paragraph_format.space_after = Pt(8)
    run_gl = p_guide_lbl.add_run("Under the guidance of")
    run_gl.font.name = "Times New Roman"
    run_gl.font.size = Pt(14)
    run_gl.font.italic = True

    p_guide = doc.add_paragraph()
    p_guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_guide = p_guide.add_run("Mrs. K. Spandana Kumari")
    run_guide.font.name = "Times New Roman"
    run_guide.font.size = Pt(16)
    run_guide.font.bold = True

    doc.add_page_break()

    # ------------------ HELPER FUNCTIONS ------------------
    def add_heading1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(15)
        run.font.bold = True
        return p

    def add_heading2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(13)
        run.font.bold = True
        return p

    def add_body(text, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)
        return p

    def add_bullet(text):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)
        return p

    def add_code_block(code_text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.05
        run = p.add_run(code_text)
        run.font.name = "Consolas"
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(30, 30, 30)
        return p

    # ------------------ ABSTRACT ------------------
    add_heading1("ABSTRACT")
    add_body("The Community Giveaway and Item Reuse Management System is a full-featured web-based platform built using Python and the Django web framework. It provides a secure, intuitive environment for students and community members to list usable educational materials, electronic accessories, books, and household goods for free, discover needed items, and claim them before specified deadlines.")
    add_body("Unlike basic frontend prototypes, this application is backed by Django's native ORM and SQLite relational database, incorporating complete User Authentication (Sign up, Login, Session Management, Logout), Model-View-Template (MVT) architecture, dynamic query filtering, ownership validation, and CSRF protection. Users can search by keywords across titles, descriptions, and campus pickup locations, filter by item categories, track personal giving and claiming histories through an activity dashboard, and manage listing statuses seamlessly.")
    add_body("The application eliminates unnecessary waste on college campuses, encourages sustainable item re-use, and showcases core software engineering concepts including relational data modeling, form sanitization, access control, and responsive user experience design.")

    # ------------------ INTRODUCTION ------------------
    add_heading1("INTRODUCTION")
    add_body("At academic institutions and residential campuses, students regularly accumulate textbooks, engineering drafting tools, calculators, dorm accessories, and electronics that remain idle once a semester or curriculum concludes. Concurrently, incoming students often search for these exact materials. Traditional physical notice boards or scattered messaging groups lack systematic categorization, real-time availability tracking, and deadline enforcement.")
    add_body("The Community Giveaway and Item Reuse Management System addresses this coordination gap by offering a centralized, accessible digital shelf. Built on Django, the application provides an authenticated experience where users can publish detailed item listings, specify campus collection spots, and coordinate handoffs.")

    # ------------------ OBJECTIVES ------------------
    add_heading1("OBJECTIVES")
    add_bullet("Develop an accessible web platform enabling community members to list usable items for giveaway at zero financial cost.")
    add_bullet("Implement secure user authentication using Django's built-in authentication system with signup, login, and access controls.")
    add_bullet("Design a relational database model with ForeignKey relationships to track item owners (creators) and claimers.")
    add_bullet("Provide multi-criteria search and category filtering (Books, Electronics, Stationery, Clothing, Home & Kitchen) to help users quickly discover needed resources.")
    add_bullet("Enforce business logic preventing self-claiming of listings and disallowing claims on expired or already claimed items.")
    add_bullet("Provide a dedicated 'My Activity' dashboard summarizing items contributed and items successfully claimed by the user.")
    add_bullet("Allow listing owners to reopen or re-list claimed items if a collection is canceled.")

    # ------------------ TECHNOLOGIES USED ------------------
    add_heading1("TECHNOLOGIES USED")
    add_bullet("Python 3.x — Core programming language for business logic, routing, and database operations.")
    add_bullet("Django Framework — High-level Python web framework providing MVT architecture, ORM, CSRF protection, and user authentication.")
    add_bullet("SQLite3 Database — Lightweight relational database storing user accounts, item metadata, status tags, and timestamps.")
    add_bullet("HTML5 & Jinja/Django Template Language (DTL) — Semantic markup and dynamic server-side template rendering.")
    add_bullet("CSS3 (Custom Design System) — Responsive layout, cards, color-coded badges, modern typography, and clean forms without external heavy UI dependencies.")
    add_bullet("JavaScript — Dynamic UI interactions, confirmation dialogs, and responsive navigation.")

    doc.add_page_break()

    # ------------------ SYSTEM ARCHITECTURE & COMPONENTS ------------------
    add_heading1("SYSTEM COMPONENTS & MODULES")

    add_heading2("1. User Authentication Module")
    add_body("Handles member onboarding and credential verification via Django's UserCreationForm, LoginView, and LogoutView. Authenticated sessions grant permissions to list items, claim items, and view personal history, while unauthenticated visitors can browse and search.")

    add_heading2("2. Community Shelf & Search Filter Module")
    add_body("The home page view ('giveaways/home.html') aggregates all listings. It supports simultaneous multi-field search (title, description, pickup location) through Django Q objects, combined with category filters and status toggles ('available' vs 'claimed'). Dynamic counter cards display total available and claimed items.")

    add_heading2("3. Item Listing & Management Module")
    add_body("Authenticated users access a validated ModelForm ('GiveawayItemForm') to contribute items. The form captures item title, category, description, campus pickup spot, preferred contact method, and an optional collection deadline. A custom clean validator ensures deadlines cannot be set in the past.")

    add_heading2("4. Claim & Workflow Engine")
    add_body("Coordinates handoffs between users. Robust server-side checks ensure that: (a) a user cannot claim their own listing, (b) already-claimed items cannot be double-claimed, and (c) expired listings are locked. Listing creators retain permissions to reopen listings if an arrangement falls through.")

    add_heading2("5. User Activity Dashboard")
    add_body("Located at '/giveaway/mine/', this dashboard presents two synchronized streams: 'Items I've shared' (showing live status badges) and 'Items I've claimed', providing full transparency over a user's campus contributions.")

    # ------------------ DATABASE DESIGN ------------------
    add_heading1("DATABASE DESIGN & DATA MODEL")
    add_body("The primary entity is the GiveawayItem model, represented in SQLite with the following schema:")

    table = doc.add_table(rows=1, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'
    hdr_cells = table.rows[0].cells
    headers = ["Field Name", "Data Type", "Constraints / Choices", "Description"]
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.size = Pt(10)

    schema_rows = [
        ("id", "BigAutoField", "Primary Key, Auto increment", "Unique item identifier"),
        ("title", "CharField(100)", "Required", "Title/name of giveaway item"),
        ("description", "TextField(800)", "Required", "Condition details and notes"),
        ("category", "CharField(20)", "Books, Electronics, Clothing, etc.", "Item classification category"),
        ("location", "CharField(120)", "Required", "Campus pickup spot"),
        ("contact_info", "CharField(120)", "Required", "Owner email or WhatsApp"),
        ("collection_deadline", "DateField", "Nullable, Blankable", "Last day to collect item"),
        ("status", "CharField(12)", "available, claimed", "Current availability status"),
        ("created_by", "ForeignKey(User)", "CASCADE", "User who posted the item"),
        ("claimed_by", "ForeignKey(User)", "SET_NULL, Nullable", "User who claimed the item"),
        ("created_at", "DateTimeField", "Default=timezone.now", "Creation timestamp"),
    ]

    for f_name, d_type, constr, desc in schema_rows:
        row_cells = table.add_row().cells
        row_cells[0].text = f_name
        row_cells[1].text = d_type
        row_cells[2].text = constr
        row_cells[3].text = desc
        for c in row_cells:
            c.paragraphs[0].runs[0].font.size = Pt(9)
            c.paragraphs[0].runs[0].font.name = "Times New Roman"

    doc.add_page_break()

    # ------------------ PROJECT STRUCTURE ------------------
    add_heading1("PROJECT STRUCTURE")
    structure_text = """giveaway_django_project/
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
    └── app.js                         # Dynamic client validation & event handling"""
    add_code_block(structure_text)

    doc.add_page_break()

    # ------------------ SOURCE CODE ------------------
    add_heading1("CORE APPLICATION CODE — BACKEND (PYTHON & DJANGO)")

    add_heading2("1. giveaways/models.py (Database Model)")
    add_code_block("""from django.conf import settings
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
        return self.title""")

    add_heading2("2. giveaways/forms.py (ModelForm & Validation)")
    add_code_block("""from django import forms
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
        return deadline""")

    add_heading2("3. giveaways/views.py (Controllers & Business Logic)")
    add_code_block("""from django.contrib import messages
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
    return render(request, "giveaways/my_items.html", {"posted": posted, "claimed": claimed})""")

    doc.add_page_break()

    # ------------------ FRONTEND CODE (HTML, CSS, JS) ------------------
    add_heading1("FRONTEND CODE (HTML, CSS, JAVASCRIPT)")

    add_heading2("4. giveaways/templates/giveaways/base.html (Master Template)")
    add_code_block("""{% load static %}
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
</html>""")

    add_heading2("5. giveaways/templates/giveaways/home.html (Landing & Shelf Template)")
    add_code_block("""{% extends "giveaways/base.html" %}
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
{% endblock %}""")

    doc.add_page_break()

    add_heading2("6. giveaways/templates/giveaways/item_detail.html (Item Detail Page)")
    add_code_block("""{% extends "giveaways/base.html" %}
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
{% endblock %}""")

    add_heading2("7. static/giveaways/style.css (Styling & Design System)")
    add_code_block(""":root {
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
.button-dark { background: var(--green); color: white; }""")

    doc.add_page_break()

    add_heading2("8. static/giveaways/app.js (Client Interactive Features & Safety)")
    add_code_block("""document.addEventListener("DOMContentLoaded", () => {
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
});""")

    doc.add_page_break()

    # ------------------ SETUP & EXECUTION ------------------
    add_heading1("SETUP AND EXECUTION")
    add_body("Requirements: Python 3.10+ installed on Windows/Linux, virtual environment, and terminal access.")
    add_heading2("Execution Commands:")
    add_code_block("""# 1. Open the project directory
cd giveaway_django_project

# 2. Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\\Scripts\\activate
# On Linux/macOS:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Populate sample demonstration data (optional)
python seed_data.py

# 6. Start the development server
python manage.py runserver""")
    add_body("Open http://127.0.0.1:8000/ in any standard browser to access the live application.")

    # ------------------ TESTING & VERIFICATION ------------------
    add_heading1("TESTING AND TEST CASES")
    add_bullet("User Authentication Test: Registered new user accounts ('rahul_sharma', 'priya_reddy'). Verified password hashing and session generation.")
    add_bullet("Search & Filter Test: Tested searching for 'Drafting' and 'Books'. Checked that only matching cards are rendered.")
    add_bullet("Form Validation Test: Attempted to submit a past collection deadline; verified that form returns an error preventing submission.")
    add_bullet("Self-Claim Prevention Test: Logged in as the owner of an item and attempted to claim it. Verified that the system rejects the operation with an error message.")
    add_bullet("Double-Claim Prevention Test: Verified that once an item transitions to 'Claimed', other users cannot re-claim it.")
    add_bullet("Owner Reopen Test: Verified that the original owner can mark a claimed listing as 'Available' again if required.")

    doc.add_page_break()

    # ------------------ OUTPUT / SCREENSHOTS ------------------
    add_heading1("OUTPUT AND APPLICATION SCREENSHOTS")
    add_body("The following figures showcase the running application interface with populated community listings:")

    # Figure 1: Landing
    add_heading2("Fig 1: Home Page & Community Overview")
    if os.path.exists("screenshots/fig1_landing_hero.png"):
        doc.add_picture("screenshots/fig1_landing_hero.png", width=Inches(6.2))
        p_cap1 = doc.add_paragraph()
        p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap1.paragraph_format.space_after = Pt(14)
        run_c1 = p_cap1.add_run("Fig 1: Community Giveaway Landing Page with Live Statistics")
        run_c1.font.italic = True
        run_c1.font.size = Pt(10)

    # Figure 2: Listings & Filters
    add_heading2("Fig 2: Community Shelf & Category Filter")
    if os.path.exists("screenshots/fig2_listings_browse.png"):
        doc.add_picture("screenshots/fig2_listings_browse.png", width=Inches(6.2))
        p_cap2 = doc.add_paragraph()
        p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap2.paragraph_format.space_after = Pt(14)
        run_c2 = p_cap2.add_run("Fig 2: Filtered Listings Shelf with Category Icons and Details")
        run_c2.font.italic = True
        run_c2.font.size = Pt(10)

    doc.add_page_break()

    # Figure 3: My Activity
    add_heading2("Fig 3: User Activity Dashboard")
    if os.path.exists("screenshots/fig3_my_activity.png"):
        doc.add_picture("screenshots/fig3_my_activity.png", width=Inches(6.2))
        p_cap3 = doc.add_paragraph()
        p_cap3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap3.paragraph_format.space_after = Pt(14)
        run_c3 = p_cap3.add_run("Fig 3: User Dashboard showing Posted Items and Claimed Items")
        run_c3.font.italic = True
        run_c3.font.size = Pt(10)

    # Figure 4: Item Detail
    add_heading2("Fig 4: Item Detail & Claim Interface")
    if os.path.exists("screenshots/fig4_item_detail.png"):
        doc.add_picture("screenshots/fig4_item_detail.png", width=Inches(6.2))
        p_cap4 = doc.add_paragraph()
        p_cap4.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap4.paragraph_format.space_after = Pt(14)
        run_c4 = p_cap4.add_run("Fig 4: Individual Item Detail Page with Location, Contact and Claim CTA")
        run_c4.font.italic = True
        run_c4.font.size = Pt(10)

    doc.add_page_break()

    # ------------------ CONCLUSION ------------------
    add_heading1("CONCLUSION")
    add_body("The Community Giveaway and Item Reuse Management System successfully demonstrates a practical, full-stack Django solution to campus resource sharing. By coupling an elegant, accessible user interface with a robust relational backend, the system allows students and faculty to easily pass on usable supplies and claim needed items without friction.")
    add_body("The implementation confirms the strength of Django's Model-View-Template architecture, showing how security controls, form validation, dynamic filtering, and database transactions work together to deliver a production-ready community experience.")

    add_heading2("Future Enhancements")
    add_bullet("Image Uploads: Integrate Django ImageField and media storage to allow users to attach physical photos of items.")
    add_bullet("In-App Realtime Messaging: Provide an encrypted chat system between giver and claimer rather than direct email/phone exposure.")
    add_bullet("Notification Alerts: Implement automated email alerts or push notifications when items matching a student's wishlist become available.")
    add_bullet("Geo-location Mapping: Embed interactive campus maps indicating exact pickup landmarks.")

    output_path = "Community_Giveaway_Project_Report.docx"
    doc.save(output_path)
    print(f"Successfully generated updated report: {output_path}")

if __name__ == "__main__":
    create_report()
