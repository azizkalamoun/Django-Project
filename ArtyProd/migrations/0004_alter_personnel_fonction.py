# Generated by Django 4.1.7 on 2023-04-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personnel',
            name='fonction',
            field=models.CharField(default='', max_length=30),
        ),
    ]