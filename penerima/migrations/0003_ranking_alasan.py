# Generated by Django 4.1.5 on 2023-07-16 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penerima', '0002_ranking_nilai'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='alasan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]