# Generated by Django 3.2 on 2022-11-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_ebook_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='aaaa', max_length=100),
        ),
    ]
