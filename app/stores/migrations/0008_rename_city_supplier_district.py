# Generated by Django 3.2.5 on 2021-07-18 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_supplier_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='city',
            new_name='district',
        ),
    ]
