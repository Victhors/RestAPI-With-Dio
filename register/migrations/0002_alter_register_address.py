# Generated by Django 4.2.5 on 2023-10-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
