# Generated by Django 2.0 on 2018-06-08 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_data', '0004_auto_20180608_2009'),
        ('competition_system', '0003_auto_20180608_2005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='often',
            new_name='offer',
        ),
        migrations.AlterModelOptions(
            name='offer',
            options={'verbose_name': 'offer', 'verbose_name_plural': 'offers'},
        ),
    ]
