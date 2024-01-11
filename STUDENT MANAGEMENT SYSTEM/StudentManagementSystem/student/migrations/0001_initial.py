# Generated by Django 4.2.7 on 2024-01-10 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]
