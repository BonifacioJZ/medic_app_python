# Generated by Django 4.2.13 on 2024-07-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergies', '0002_allergies_created_at_allergies_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='allergies',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]