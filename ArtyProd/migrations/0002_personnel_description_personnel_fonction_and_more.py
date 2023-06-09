# Generated by Django 4.1.7 on 2023-04-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnel',
            name='description',
            field=models.CharField(default='No description provided', max_length=100),
        ),
        migrations.AddField(
            model_name='personnel',
            name='fonction',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='personnel',
            name='lien_facebook',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personnel',
            name='lien_github',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personnel',
            name='lien_twitter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='fichier_CV',
            field=models.FileField(null=True, upload_to='pdf_files/'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='lien_linkedln',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='nom',
            field=models.CharField(max_length=20),
        ),
    ]
