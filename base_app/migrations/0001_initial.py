# Generated by Django 3.1.5 on 2021-01-12 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('estimated_value', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('CL', 'Clothing'), ('ED', 'Electronics & Devices'), ('KD', 'Kids'), ('FI', 'Food Items'), ('KI', 'Kitchen'), ('FH', 'Furniture & Housing')], max_length=2)),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=400)),
                ('condition', models.CharField(choices=[('N', 'New'), ('U', 'Used')], max_length=1)),
                ('image', models.ImageField(upload_to='')),
                ('image_1', models.ImageField(upload_to='')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('response_date', models.DateTimeField(blank=True, null=True)),
                ('accepted', models.BooleanField(blank=True, default=False, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=20)),
                ('phone_1', models.CharField(blank=True, max_length=15)),
                ('phone_2', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
