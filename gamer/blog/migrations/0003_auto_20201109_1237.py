# Generated by Django 3.1.2 on 2020-11-09 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201002_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time']},
        ),
    ]