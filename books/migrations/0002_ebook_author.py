# Generated by Django 3.2 on 2022-11-25 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='author',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]