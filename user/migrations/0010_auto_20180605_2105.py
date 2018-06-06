# Generated by Django 2.0 on 2018-06-05 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20180604_2000'),
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
