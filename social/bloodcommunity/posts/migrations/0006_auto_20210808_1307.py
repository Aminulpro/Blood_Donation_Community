# Generated by Django 3.2.4 on 2021-08-08 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210807_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contact',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='donation_date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='donation_time',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
