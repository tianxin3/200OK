# Generated by Django 2.1.5 on 2020-03-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0026_auto_20200309_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='unlisted',
            field=models.BooleanField(choices=[(False, 'False'), (True, 'True')], default=False),
        ),
    ]
