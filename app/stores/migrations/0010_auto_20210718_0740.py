# Generated by Django 3.2.5 on 2021-07-18 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_receivegood_purchase_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliverygood',
            old_name='received_comment',
            new_name='delivery_comment',
        ),
        migrations.RenameField(
            model_name='deliverygood',
            old_name='received_date',
            new_name='delivery_date',
        ),
        migrations.RenameField(
            model_name='deliverygood',
            old_name='received_by',
            new_name='delivery_from',
        ),
        migrations.RenameField(
            model_name='deliverygood',
            old_name='received_from',
            new_name='delivery_to',
        ),
    ]
