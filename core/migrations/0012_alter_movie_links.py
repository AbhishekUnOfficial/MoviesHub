# Generated by Django 4.2.6 on 2023-10-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_movie_links_movie_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='links',
            field=models.ManyToManyField(to='core.link'),
        ),
    ]
