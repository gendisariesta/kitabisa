# Generated by Django 4.1.5 on 2023-04-18 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dtks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penerima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_bukti', models.ImageField(null=True, upload_to='bukti/')),
                ('tahun', models.CharField(blank=True, max_length=10, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Dalam Proses', 'Dalam Proses'), ('Diterima', 'Diterima')], default='Dalam Proses', max_length=60)),
                ('anggota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dtks.anggota')),
                ('bansos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dtks.bansos')),
            ],
        ),
    ]
