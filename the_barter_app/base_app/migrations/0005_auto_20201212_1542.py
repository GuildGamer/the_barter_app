# Generated by Django 3.0.5 on 2020-12-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(max_length=30),
        ),
    ]
