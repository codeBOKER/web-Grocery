# Generated by Django 3.0.5 on 2023-10-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20231029_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATch_cat',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Category'),
        ),
    ]
