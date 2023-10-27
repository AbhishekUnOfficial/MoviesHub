# Generated by Django 4.2.6 on 2023-10-26 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_rename_language_movie_languages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='posted',
            new_name='published',
        ),
        migrations.AddField(
            model_name='movie',
            name='updated',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]