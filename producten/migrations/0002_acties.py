# Generated by Django 4.0.1 on 2022-01-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producten', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('beschrijving', models.CharField(max_length=255)),
                ('korting', models.FloatField()),
            ],
        ),
    ]