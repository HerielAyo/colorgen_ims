# Generated by Django 4.0.3 on 2023-12-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='tin_size',
            field=models.CharField(max_length=10),
        ),
    ]
