# Generated by Django 3.2.9 on 2021-12-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-03-04'),
            preserve_default=False,
        ),
    ]
