# Generated by Django 3.0.2 on 2020-01-24 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0002_auto_20200124_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('borrower_id', models.IntegerField(primary_key=True, serialize=False)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('return_date', models.DateField()),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_api.Books')),
            ],
        ),
    ]
