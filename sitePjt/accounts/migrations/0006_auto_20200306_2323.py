# Generated by Django 2.1.5 on 2020-03-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200305_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatar/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.CharField(default='8f8a32cc-f81b-4906-9950-32cddcfbc0d4', editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='url',
            field=models.URLField(default='8f8a32cc-f81b-4906-9950-32cddcfbc0d4', max_length=100),
        ),
    ]
