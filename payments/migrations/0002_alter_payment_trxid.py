# Generated by Django 4.2.9 on 2025-02-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='trxid',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
