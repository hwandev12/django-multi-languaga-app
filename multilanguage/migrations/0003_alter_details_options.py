# Generated by Django 4.0.4 on 2022-05-09 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multilanguage', '0002_details_name_en_details_name_uz_details_text_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name': 'Detail', 'verbose_name_plural': 'Details'},
        ),
    ]