# Generated by Django 4.1.6 on 2023-05-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clustering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenis',
            name='ac',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='babi',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='gas',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='kambing',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='kapal',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='kerbau',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='komputer',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='kuda',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='kulkas',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='lahan',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='luas_bangunan',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='luas_lahan',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='mobil',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='motor',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='motor_tempel',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='pemanas_air',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='perahu',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='perahu_motor',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='perhiasan',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='sapi',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='sepeda',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='telepon_rumah',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='tv',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jenis',
            name='unggas',
            field=models.BooleanField(default=False, null=True),
        ),
    ]