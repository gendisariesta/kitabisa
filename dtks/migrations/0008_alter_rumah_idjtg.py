# Generated by Django 4.1.6 on 2023-07-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtks', '0007_alter_rumah_idjtg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rumah',
            name='IDJTG',
            field=models.BigIntegerField(),
        ),
    ]