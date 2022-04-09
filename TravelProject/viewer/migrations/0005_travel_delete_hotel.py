# Generated by Django 4.0.3 on 2022-04-09 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0004_country_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_departure', models.DateField()),
                ('date_of_return', models.DateField()),
                ('people', models.IntegerField()),
                ('type', models.CharField(max_length=15)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='viewer.city')),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]