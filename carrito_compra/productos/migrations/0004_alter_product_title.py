# Generated by Django 4.0 on 2021-12-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
