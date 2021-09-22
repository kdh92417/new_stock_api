# Generated by Django 3.2.7 on 2021-09-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='portfolio',
            field=models.ManyToManyField(related_name='user_portfolio', through='portfolio.LikePortfolio', to='portfolio.Portfolio'),
        ),
    ]
