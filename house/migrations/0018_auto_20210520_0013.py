# Generated by Django 3.1.2 on 2021-05-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0017_expense_maker_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='tenant',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='tenant',
        ),
        migrations.AddField(
            model_name='expense',
            name='title',
            field=models.CharField(default='good', max_length=100),
            preserve_default=False,
        ),
    ]
