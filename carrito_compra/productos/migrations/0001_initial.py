# Generated by Django 4.0 on 2021-12-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
