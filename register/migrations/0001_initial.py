# Generated by Django 4.2.5 on 2023-10-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Registration Form',
            },
        ),
    ]
