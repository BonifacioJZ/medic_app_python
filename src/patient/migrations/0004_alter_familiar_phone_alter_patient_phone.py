# Generated by Django 4.2.13 on 2024-06-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_familiar_city_alter_familiar_colony_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='phone',
            field=models.CharField(blank=True, default='000-000-0000', max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, default='000-000-0000', max_length=13, null=True),
        ),
    ]
