# Generated by Django 4.2.3 on 2023-07-31 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_sizevariant_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="color_variant",
            field=models.ManyToManyField(blank=True, to="products.colorvariant"),
        ),
        migrations.AlterField(
            model_name="product",
            name="size_variant",
            field=models.ManyToManyField(blank=True, to="products.sizevariant"),
        ),
    ]
