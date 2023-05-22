# Generated by Django 4.1.7 on 2023-04-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0002_personnel_description_personnel_fonction_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localisation', models.CharField(max_length=50)),
                ('numéro_tel', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]