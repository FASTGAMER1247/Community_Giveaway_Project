from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import GiveawayItemForm
from .models import GiveawayItem

def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account is ready. You can now post or claim items.")
        return redirect("home")
    return render(request, "giveaways/signup.html", {"form": form})

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
    return render(request, "giveaways/item_form.html", {"form": form, "page_title": "Give something away"})

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
        messages.error(request, "The collection deadline has passed; this listing cannot be claimed.")
    else:
        item.status = "claimed"
        item.claimed_by = request.user
        item.save(update_fields=["status", "claimed_by"])
        messages.success(request, "Item marked as claimed. Contact the giver to arrange collection.")
    return redirect("item_detail", pk=pk)

@login_required
def mark_available(request, pk):
    item = get_object_or_404(GiveawayItem, pk=pk)
    if item.created_by_id != request.user.id:
        return HttpResponseForbidden("Only the person who posted this item can reopen it.")
    if request.method == "POST":
        item.status = "available"
        item.claimed_by = None
        item.save(update_fields=["status", "claimed_by"])
        messages.success(request, "Your listing is available again.")
    return redirect("item_detail", pk=pk)

@login_required
def my_items(request):
    posted = GiveawayItem.objects.filter(created_by=request.user)
    claimed = GiveawayItem.objects.filter(claimed_by=request.user)
    return render(request, "giveaways/my_items.html", {"posted": posted, "claimed": claimed})
