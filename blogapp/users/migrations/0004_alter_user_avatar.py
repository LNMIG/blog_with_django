# Generated by Django 4.2.2 on 2023-06-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, default={'C:\\z Mis Repos\\informatorio\\blog_with_django\\blogapp\\media/basic_avatar.svg'}, max_length=500, null=True),
        ),
    ]
