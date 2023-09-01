# Generated by Django 4.2.4 on 2023-08-28 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_typesession_name'),
        ('login', '0003_acount_imgavatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='acount',
            name='typeAccount',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='agenda.typesession'),
        ),
        migrations.AlterField(
            model_name='acount',
            name='imgAvatar',
            field=models.ImageField(default='avatares/avatar.png', upload_to='avatares/'),
        ),
    ]
