# Generated by Django 2.0 on 2018-06-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='often',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_work', models.IntegerField(max_length=4)),
            ],
            options={
                'verbose_name': 'often',
                'verbose_name_plural': 'oftens',
            },
        ),
    ]
