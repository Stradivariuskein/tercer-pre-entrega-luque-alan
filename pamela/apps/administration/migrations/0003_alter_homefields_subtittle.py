# Generated by Django 4.2.4 on 2023-09-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_rename_home_values_homefields_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homefields',
            name='subTittle',
            field=models.CharField(max_length=200),
        ),
    ]