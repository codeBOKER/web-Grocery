# Generated by Django 3.0.5 on 2023-11-02 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20231031_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productalternative',
            name='PALTRalternative',
            field=models.ManyToManyField(related_name='product_alternatives', to='main.Product'),
        ),
    ]
