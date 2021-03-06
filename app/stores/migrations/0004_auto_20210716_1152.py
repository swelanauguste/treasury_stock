# Generated by Django 3.2.5 on 2021-07-16 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_alter_supplier_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='count',
            new_name='qty',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_received',
        ),
        migrations.RemoveField(
            model_name='product',
            name='purchase_order',
        ),
        migrations.RemoveField(
            model_name='product',
            name='qty_ordered',
        ),
        migrations.RemoveField(
            model_name='product',
            name='qty_received',
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_suppliers', to='stores.supplier'),
        ),
    ]
