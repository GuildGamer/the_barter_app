# Generated by Django 3.0.5 on 2020-12-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0010_auto_20201216_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_uploaded',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
