# Generated by Django 4.0 on 2021-12-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
            preserve_default=False,
        ),
    ]