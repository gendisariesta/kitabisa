# Generated by Django 4.1.6 on 2023-07-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penerima', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='alasan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]