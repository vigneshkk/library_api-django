# Generated by Django 3.0.2 on 2020-01-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
