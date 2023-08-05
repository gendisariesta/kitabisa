# Generated by Django 4.1.6 on 2023-07-19 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dtks', '0011_alter_rumah_idjtg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kriteria', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot', models.IntegerField(blank=True, null=True)),
                ('atribut', models.CharField(choices=[('Benefit', 'Benefit'), ('Cost', 'Cost')], max_length=30)),
                ('bansos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dtks.bansos')),
            ],
        ),
        migrations.CreateModel(
            name='Crips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_crips', models.CharField(blank=True, max_length=50, null=True)),
                ('bobot_crips', models.IntegerField(blank=True, null=True)),
                ('bansos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dtks.bansos')),
                ('kriteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranking.kriteria')),
            ],
        ),
    ]
