# Generated by Django 3.2.9 on 2021-12-17 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_auto_20211213_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workerthread',
            name='pool',
        ),
        migrations.AddField(
            model_name='workerpool',
            name='code',
            field=models.CharField(default='GeraIntegracaoVendas', max_length=100),
            preserve_default=False,
        ),
    ]
