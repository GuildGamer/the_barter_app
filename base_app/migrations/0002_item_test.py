# Generated by Django 3.1.5 on 2021-01-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='test',
            field=models.CharField(default='yo', max_length=100),
            preserve_default=False,
        ),
    ]