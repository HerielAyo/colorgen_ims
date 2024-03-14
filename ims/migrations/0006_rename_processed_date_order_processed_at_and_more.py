# Generated by Django 4.0.3 on 2023-12-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0005_alter_order_processed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='processed_date',
            new_name='processed_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='processed',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'processed'), (0, 'not processed')], default=0),
        ),
    ]
