# Generated by Django 4.2.6 on 2023-10-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]