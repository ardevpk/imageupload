# Generated by Django 4.0.3 on 2022-03-24 07:39

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=254)),
                ('numofimages', models.IntegerField()),
                ('image', models.ImageField(upload_to=app.models.getcurrentusername)),
            ],
        ),
    ]
