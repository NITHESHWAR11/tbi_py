# Generated by Django 3.2.4 on 2023-07-12 09:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_mentor_lists'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center_of_excellance',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title_iot', models.CharField(max_length=200)),
                ('contant_iot', models.CharField(max_length=200)),
                ('image_iot', models.ImageField(upload_to='center_of_excellance_images/')),
                ('uplode_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Design_And_Development',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title_iot', models.CharField(max_length=200)),
                ('contant_iot', models.CharField(max_length=200)),
                ('image_iot', models.ImageField(upload_to='design_and_development_images/')),
                ('uplode_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HealthCare_form',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title_iot', models.CharField(max_length=200)),
                ('contant_iot', models.CharField(max_length=200)),
                ('image_iot', models.ImageField(upload_to='HealthCare_images/')),
                ('uplode_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Iot_form',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title_iot', models.CharField(max_length=200)),
                ('contant_iot', models.CharField(max_length=200)),
                ('image_iot', models.ImageField(upload_to='Iot_images/')),
                ('uplode_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Support_servise',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title_iot', models.CharField(max_length=200)),
                ('contant_iot', models.CharField(max_length=200)),
                ('image_iot', models.ImageField(upload_to='support_servise_images/')),
                ('uplode_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]