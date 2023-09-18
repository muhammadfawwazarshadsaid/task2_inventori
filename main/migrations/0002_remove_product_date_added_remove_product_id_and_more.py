# Generated by Django 4.2.5 on 2023-09-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="date_added",),
        migrations.RemoveField(model_name="product", name="id",),
        migrations.AddField(
            model_name="product",
            name="amount",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="no",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product", name="price", field=models.PositiveIntegerField(),
        ),
    ]