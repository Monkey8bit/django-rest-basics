# Generated by Django 3.2.12 on 2022-04-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220411_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduleruser',
            name='username',
        ),
        migrations.AlterField(
            model_name='scheduleruser',
            name='user_name',
            field=models.CharField(max_length=60),
        ),
    ]
