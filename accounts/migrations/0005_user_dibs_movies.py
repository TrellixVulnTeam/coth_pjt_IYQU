# Generated by Django 3.1.2 on 2020-11-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20201122_1000'),
        ('accounts', '0004_auto_20201121_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dibs_movies',
            field=models.ManyToManyField(blank=True, null=True, related_name='dibs_users', to='movies.Movie'),
        ),
    ]
