# Generated by Django 4.2.13 on 2024-06-25 20:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('colony', models.CharField(max_length=100)),
                ('curp', models.CharField(max_length=18, unique=True)),
                ('birth_day', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'familiar',
                'verbose_name_plural': 'familiars',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('colony', models.CharField(max_length=100)),
                ('curp', models.CharField(max_length=18, unique=True)),
                ('birth_day', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('familiar', models.ManyToManyField(blank=True, to='patient.familiar')),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
            },
        ),
    ]
