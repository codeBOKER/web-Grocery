# Generated by Django 4.2.9 on 2024-02-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20231113_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PDCTimage',
            field=models.ImageField(blank=True, null=True, upload_to='product/<django.db.models.fields.related.ForeignKey>/%y/%m/%d', verbose_name='Image'),
        ),
    ]
