# Generated by Django 3.2.3 on 2021-07-20 05:34

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
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]