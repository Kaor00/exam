# Generated by Django 5.1.1 on 2024-09-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_remove_actors_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='film',
            field=models.ManyToManyField(to='films.filmlist'),
        ),
    ]
