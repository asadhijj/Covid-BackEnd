# Generated by Django 4.2 on 2023-04-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19', '0002_countryrecord_delete_covidrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('total_confirmed_cases', models.IntegerField()),
                ('total_deaths_cases', models.IntegerField()),
                ('total_recovered_cases', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='CountryRecord',
        ),
    ]
