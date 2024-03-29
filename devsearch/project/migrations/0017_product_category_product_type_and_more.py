# Generated by Django 4.2 on 2023-04-13 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_alter_category_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='product_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='product_price',
            field=models.IntegerField(default='цена продукта'),
        ),
        migrations.AlterField(
            model_name='category',
            name='product_category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.product_category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='roduct_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='project.product_type'),
        ),
    ]
