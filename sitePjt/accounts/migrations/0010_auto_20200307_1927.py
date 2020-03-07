# Generated by Django 2.1.5 on 2020-03-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200307_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.CharField(default='990f5084-4612-41f1-a427-7400660a76a3', editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='url',
            field=models.URLField(default='990f5084-4612-41f1-a427-7400660a76a3', max_length=100),
        ),
    ]
