# Generated by Django 4.0.3 on 2022-04-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_travel_delete_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='price',
            field=models.FloatField(default='-'),
        ),
    ]