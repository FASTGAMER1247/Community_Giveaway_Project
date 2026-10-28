from django import forms
from .models import GiveawayItem

class GiveawayItemForm(forms.ModelForm):
    class Meta:
        model = GiveawayItem
        fields = ["title", "description", "category", "location", "contact_info", "collection_deadline"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. First-year engineering textbook"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Describe the item and its condition"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control", "placeholder": "e.g. Main college gate"}),
            "contact_info": forms.TextInput(attrs={"class": "form-control", "placeholder": "Email or preferred contact method"}),
            "collection_deadline": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def clean_collection_deadline(self):
        deadline = self.cleaned_data.get("collection_deadline")
        from django.utils import timezone
        if deadline and deadline < timezone.localdate():
            raise forms.ValidationError("Collection deadline cannot be in the past.")
        return deadline
