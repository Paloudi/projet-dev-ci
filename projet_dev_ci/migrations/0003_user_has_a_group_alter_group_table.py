# Generated by Django 4.0.1 on 2022-01-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet_dev_ci', '0002_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_a_group',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='group',
            table='groups',
        ),
    ]
