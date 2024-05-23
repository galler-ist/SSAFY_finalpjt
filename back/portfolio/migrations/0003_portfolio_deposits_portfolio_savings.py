# Generated by Django 4.2.8 on 2024-05-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
        ('portfolio', '0002_remove_portfolio_savings_alter_portfolio_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='deposits',
            field=models.ManyToManyField(blank=True, related_name='deposits', to='finance.deposit'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='savings',
            field=models.ManyToManyField(blank=True, related_name='savings', to='finance.saving'),
        ),
    ]
