# Generated by Django 3.1.2 on 2021-06-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0032_auto_20210625_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='hid',
            field=models.BooleanField(default=True),
        ),
    ]
