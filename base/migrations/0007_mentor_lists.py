# Generated by Django 3.2.4 on 2023-07-03 09:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_ourstartup_images_cmp_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentor_lists',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('menter_name', models.CharField(max_length=200)),
                ('special_at', models.CharField(max_length=200)),
                ('menter_img', models.ImageField(default='images/user_image.png', upload_to='mentors_profile/%Y/%m/%d')),
                ('TECK_OR_NONTECK', models.CharField(max_length=200)),
                ('last_updated_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
