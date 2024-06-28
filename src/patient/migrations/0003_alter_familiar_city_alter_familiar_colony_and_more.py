# Generated by Django 4.2.13 on 2024-06-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_familiar_email_alter_familiar_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='familiar',
            name='colony',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='colony',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='familiar',
            field=models.ManyToManyField(blank=True, related_name='familiar', to='patient.familiar'),
        ),
    ]
