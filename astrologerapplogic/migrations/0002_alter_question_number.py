# Generated by Django 4.1.3 on 2023-01-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("astrologerapplogic", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="number",
            field=models.CharField(max_length=200),
        ),
    ]
