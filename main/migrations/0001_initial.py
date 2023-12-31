# Generated by Django 4.2.4 on 2023-09-23 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("no", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField(auto_now_add=True)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("price", models.PositiveIntegerField()),
                ("amount", models.PositiveIntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
