# Generated by Django 4.1.1 on 2022-09-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(default='NA', max_length=200),
        ),
    ]
