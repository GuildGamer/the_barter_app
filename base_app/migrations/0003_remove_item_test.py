# Generated by Django 3.1.5 on 2021-01-12 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_item_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='test',
        ),
    ]