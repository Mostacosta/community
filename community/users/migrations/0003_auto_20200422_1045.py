# Generated by Django 3.0.5 on 2020-04-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200422_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='contact',
            field=models.ManyToManyField(blank=True, to='users.contacts'),
        ),
    ]
