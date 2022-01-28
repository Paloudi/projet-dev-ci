# Generated by Django 4.0.1 on 2022-01-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet_dev_ci', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_size', models.PositiveIntegerField()),
                ('current_size', models.PositiveIntegerField()),
                ('users', models.TextField(null=True)),
            ],
        ),
    ]
