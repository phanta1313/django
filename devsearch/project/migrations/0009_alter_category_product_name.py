# Generated by Django 4.1.5 on 2023-03-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_category_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
