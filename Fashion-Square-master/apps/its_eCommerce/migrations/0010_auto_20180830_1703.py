# Generated by Django 2.1 on 2018-08-31 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('its_eCommerce', '0009_auto_20180830_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wish',
            name='product',
        ),
        migrations.AddField(
            model_name='wish',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='wishedProducts', to='its_eCommerce.Product'),
            preserve_default=False,
        ),
    ]
