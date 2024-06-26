# Generated by Django 4.2.13 on 2024-06-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]