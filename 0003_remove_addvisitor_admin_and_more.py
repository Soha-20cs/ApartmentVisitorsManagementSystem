# Generated by Django 4.1.7 on 2023-03-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avsapp', '0002_addvisitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addvisitor',
            name='admin',
        ),
        migrations.AlterField(
            model_name='addvisitor',
            name='mobilenumber',
            field=models.IntegerField(default=0),
        ),
    ]
