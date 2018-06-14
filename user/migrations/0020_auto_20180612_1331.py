# Generated by Django 2.0 on 2018-06-12 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20180608_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Profile'),
        ),
    ]
