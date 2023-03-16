# Generated by Django 4.1.5 on 2023-03-06 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='first',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default='title', max_length=255),
        ),
    ]
