# Generated by Django 2.1.5 on 2020-03-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20200309_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.CharField(default='51cd0f62-bb05-4ea2-9631-8e49ff609161', editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='url',
            field=models.URLField(default='http:127.0.0.1:8000/accounts/author/profile/51cd0f62-bb05-4ea2-9631-8e49ff609161/', max_length=100),
        ),
    ]
