# Generated by Django 5.0.4 on 2024-04-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LatLongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lattitude', models.DecimalField(decimal_places=5, max_digits=6)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=6)),
                ('distance', models.DecimalField(decimal_places=5, max_digits=6)),
            ],
        ),
    ]
