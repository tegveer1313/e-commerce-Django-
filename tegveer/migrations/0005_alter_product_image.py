# Generated by Django 3.2.3 on 2021-07-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tegveer', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='media/shop/images'),
        ),
    ]
