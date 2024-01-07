# Generated by Django 5.0 on 2024-01-03 17:09

import formApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formApp', '0002_dbproject_big_integer_field_dbproject_binary_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbproject',
            name='comma_separated_field',
            field=models.CharField(default='default,value,example', max_length=255, validators=[formApp.models.comma_separated_validator]),
        ),
    ]
