# Generated by Django 5.0 on 2024-02-16 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_rename_tourpackages_packages_tourpackage'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='packages',
            table='package_tables',
        ),
    ]
