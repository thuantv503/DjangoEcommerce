# Generated by Django 5.0.6 on 2024-07-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
