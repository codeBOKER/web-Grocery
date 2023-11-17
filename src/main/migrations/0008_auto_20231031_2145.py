# Generated by Django 3.0.5 on 2023-10-31 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20231029_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='CATpa_cat',
        ),
        migrations.AddField(
            model_name='category',
            name='CATnull_cat',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATcat__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category', verbose_name='Null category'),
        ),
    ]