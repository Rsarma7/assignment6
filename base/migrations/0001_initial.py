# Generated by Django 4.0.6 on 2022-07-20 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiry_des', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
