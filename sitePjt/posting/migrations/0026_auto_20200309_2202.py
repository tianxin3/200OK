# Generated by Django 2.1.5 on 2020-03-09 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0025_auto_20200309_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='unlisted',
            field=models.BooleanField(choices=[(True, 'True'), (False, 'False')], default=False),
        ),
    ]
