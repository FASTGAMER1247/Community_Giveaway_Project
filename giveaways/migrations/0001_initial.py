# Initial migration for GiveawayItem.
import django.conf
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        migrations.swappable_dependency(django.conf.settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.CreateModel(
            name="GiveawayItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=800)),
                ("category", models.CharField(choices=[("Books", "Books"), ("Electronics", "Electronics"), ("Clothing", "Clothing"), ("Home", "Home & Kitchen"), ("Stationery", "Stationery"), ("Other", "Other")], default="Other", max_length=20)),
                ("location", models.CharField(max_length=120)),
                ("contact_info", models.CharField(help_text="Email or preferred contact method", max_length=120)),
                ("collection_deadline", models.DateField(blank=True, null=True)),
                ("status", models.CharField(choices=[("available", "Available"), ("claimed", "Claimed")], default="available", max_length=12)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("claimed_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="claimed_items", to=django.conf.settings.AUTH_USER_MODEL)),
                ("created_by", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="giveaway_items", to=django.conf.settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
