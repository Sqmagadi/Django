# Generated by Django 5.0.6 on 2024-06-01 11:54

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_specification_product_specification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Specification',
        ),
        migrations.AddField(
            model_name='product',
            name='Specification',
            field=mptt.fields.TreeForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.specification'),
            preserve_default=False,
        ),
    ]
