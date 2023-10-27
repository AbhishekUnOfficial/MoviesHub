# Generated by Django 4.2.6 on 2023-10-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_tag_language_rename_tags_movie_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='links',
        ),
        migrations.AddField(
            model_name='movie',
            name='links',
            field=models.ManyToManyField(blank=True, null=True, to='core.link'),
        ),
    ]
