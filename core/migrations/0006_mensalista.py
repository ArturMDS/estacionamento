# Generated by Django 4.1 on 2022-09-04 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_parametro_valor_hora_alter_parametro_valor_mes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.veiculo')),
            ],
        ),
    ]
