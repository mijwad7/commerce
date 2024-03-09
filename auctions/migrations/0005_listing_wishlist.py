# Generated by Django 4.2.2 on 2023-07-11 16:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_bid_is_winning_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
