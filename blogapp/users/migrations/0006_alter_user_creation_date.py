# Generated by Django 4.2.2 on 2023-06-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
