# Generated by Django 3.0.5 on 2023-10-29 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20231029_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATch_cat',
            field=models.CharField(max_length=50, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATimage',
            field=models.ImageField(upload_to='category', verbose_name='Category image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATpa_cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category', verbose_name='Parent category'),
        ),
    ]
