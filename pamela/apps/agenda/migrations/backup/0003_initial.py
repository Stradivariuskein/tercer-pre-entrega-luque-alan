# Generated by Django 4.2.4 on 2023-08-08 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agenda', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('time_fin', models.TimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Acount')),
            ],
        ),
    ]
