# Generated by Django 5.0.6 on 2024-06-01 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_size_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Specification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.specification'),
        ),
    ]
