# Generated by Django 3.0.5 on 2023-11-10 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_category_catcat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='PDCTcateg',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
