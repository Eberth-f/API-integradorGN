# Generated by Django 3.2.9 on 2021-12-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='codigo_gera',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
