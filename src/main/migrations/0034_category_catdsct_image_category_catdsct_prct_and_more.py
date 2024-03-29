# Generated by Django 4.2.9 on 2024-02-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_category_id_alter_product_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='CATdsct_image',
            field=models.ImageField(blank=True, null=True, upload_to='discount_photos/%y/%m/%d', verbose_name='discount image'),
        ),
        migrations.AddField(
            model_name='category',
            name='CATdsct_prct',
            field=models.FloatField(default=0, verbose_name='discount percent'),
        ),
        migrations.AddField(
            model_name='product',
            name='PDCTdsct_prct',
            field=models.FloatField(default=0, verbose_name='discount percent'),
        ),
    ]
