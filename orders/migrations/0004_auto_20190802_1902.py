# Generated by Django 2.2.3 on 2019-08-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190802_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_of_fulfilment',
            field=models.DateTimeField(blank=True, null=True, verbose_name='order fulfiled'),
        ),
    ]
