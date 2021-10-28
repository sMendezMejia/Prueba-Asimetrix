# Generated by Django 3.2.8 on 2021-10-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pollo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('lesionTipo', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
                ('lesionRango', models.CharField(max_length=20, null=True)),
                ('granja', models.CharField(max_length=100, null=True)),
                ('edadEnDias', models.IntegerField(null=True)),
                ('ciclo', models.IntegerField(null=True)),
                ('noGalpon', models.IntegerField(null=True)),
                ('planVacuna', models.CharField(max_length=100, null=True)),
                ('influenzaVacuna', models.CharField(max_length=100, null=True)),
                ('newcastleVacuna', models.CharField(max_length=100, null=True)),
                ('gumboroVacuna', models.CharField(max_length=100, null=True)),
                ('lesionPromedio', models.IntegerField(null=True)),
                ('nAnimal', models.IntegerField(null=True)),
                ('sexoAnimales', models.CharField(max_length=20, null=True)),
                ('bursometro', models.IntegerField(null=True)),
                ('condicionHigado', models.CharField(max_length=20, null=True)),
                ('integridadIntestinal', models.IntegerField(null=True)),
            ],
        ),
    ]
