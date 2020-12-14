# Generated by Django 3.0.5 on 2020-12-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, choices=[('CL', 'Clothing'), ('ED', 'Electronics & Devices'), ('KD', 'Kids'), ('FI', 'Food Items'), ('KI', 'Kitchen'), ('FH', 'Furniture & Housing')], max_length=2, null=True),
        ),
    ]
