# Generated by Django 3.1.2 on 2021-05-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0015_auto_20210508_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='maker_name',
            field=models.CharField(default='sekisuiheim', max_length=100),
            preserve_default=False,
        ),
    ]
