# Generated by Django 3.0.5 on 2023-11-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20231110_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PDCTquant',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity'),
        ),
    ]
