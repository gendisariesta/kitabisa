# Generated by Django 4.1.6 on 2023-06-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_cluster', models.CharField(max_length=100)),
                ('jumlah_k', models.IntegerField()),
            ],
        ),
    ]
