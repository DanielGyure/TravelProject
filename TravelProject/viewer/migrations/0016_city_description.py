# Generated by Django 4.0.3 on 2022-04-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0015_travel_description_travel_name_alter_travel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
