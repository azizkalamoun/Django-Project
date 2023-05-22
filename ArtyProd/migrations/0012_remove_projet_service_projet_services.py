# Generated by Django 4.1.7 on 2023-05-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0011_service_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='service',
        ),
        migrations.AddField(
            model_name='projet',
            name='services',
            field=models.ManyToManyField(to='ArtyProd.service'),
        ),
    ]
