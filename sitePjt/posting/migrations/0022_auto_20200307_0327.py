# Generated by Django 2.1.5 on 2020-03-07 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0021_auto_20200307_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_type',
            field=models.CharField(choices=[('md', 'text/markdown'), ('text', 'text/plain')], default='text', max_length=4),
        ),
    ]
