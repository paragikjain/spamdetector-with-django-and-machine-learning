# Generated by Django 2.1.7 on 2019-04-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spamdb',
            name='data',
            field=models.CharField(max_length=5000),
        ),
    ]