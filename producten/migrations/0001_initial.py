# Generated by Django 4.0.1 on 2022-01-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=155)),
                ('prijs', models.FloatField()),
                ('actieprijs', models.FloatField()),
                ('voorraad', models.IntegerField()),
                ('description', models.TextField()),
                ('afbeelding', models.TextField(max_length=2083)),
            ],
        ),
    ]
