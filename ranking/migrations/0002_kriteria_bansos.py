# Generated by Django 4.1.5 on 2023-07-17 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtks', '0006_rumah_jum_anggota'),
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kriteria',
            name='bansos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dtks.bansos'),
        ),
    ]