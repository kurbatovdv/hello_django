# Generated by Django 2.2.5 on 2019-09-27 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_license_astor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license_astor',
            name='shop',
        ),
        migrations.AddField(
            model_name='shop',
            name='license_astor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hello.License_Astor'),
        ),
    ]
