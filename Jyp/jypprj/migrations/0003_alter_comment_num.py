# Generated by Django 3.2.7 on 2021-11-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jypprj', '0002_auto_20211129_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='num',
            field=models.CharField(max_length=250, null=True, verbose_name='작성위치'),
        ),
    ]