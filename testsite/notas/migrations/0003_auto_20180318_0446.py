# Generated by Django 2.0.3 on 2018-03-18 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0002_auto_20180316_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('data', models.DateField(blank=True)),
                ('descricao', models.CharField(max_length=70)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('tipo_gasto', models.CharField(choices=[('Serviços', 'SERVIÇOS'), ('Ferramentas', 'FERRAMENTAS')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='NotasCompra',
        ),
    ]
