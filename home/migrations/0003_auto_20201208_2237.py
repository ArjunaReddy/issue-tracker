# Generated by Django 3.1.3 on 2020-12-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201205_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
