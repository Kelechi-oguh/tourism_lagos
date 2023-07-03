# Generated by Django 4.2.1 on 2023-06-28 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_managers_alter_customuser_email'),
        ('place', '0003_alter_place_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketList',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('places', models.ManyToManyField(to='place.place')),
            ],
        ),
    ]