# Generated by Django 5.0 on 2024-02-16 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_packages_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='packages',
            table='package_table',
        ),
    ]
