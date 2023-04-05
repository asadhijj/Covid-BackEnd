# Generated by Django 4.2 on 2023-04-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CovidRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('total_confirmed', models.IntegerField()),
                ('total_deaths', models.IntegerField()),
                ('total_recovered', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]