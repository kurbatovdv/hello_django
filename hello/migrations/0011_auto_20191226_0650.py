# Generated by Django 2.2.5 on 2019-12-26 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20191226_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge_journal',
            name='time',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Время выдачи'),
        ),
    ]
