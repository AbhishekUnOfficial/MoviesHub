# Generated by Django 4.2.6 on 2023-10-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_movie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]