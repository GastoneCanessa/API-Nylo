# Generated by Django 3.2.17 on 2023-05-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_name_sold_item_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
