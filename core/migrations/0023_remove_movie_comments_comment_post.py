# Generated by Django 4.2.6 on 2023-10-31 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_movie_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.movie'),
        ),
    ]
