# Generated by Django 5.1.2 on 2024-11-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RehabiliationCenter',
            fields=[
                ('center_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('location', models.TextField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
