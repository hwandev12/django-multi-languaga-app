# Generated by Django 4.0.4 on 2022-05-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multilanguage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='text_uz',
            field=models.TextField(null=True),
        ),
    ]
