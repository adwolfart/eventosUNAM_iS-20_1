# Generated by Django 2.2.5 on 2019-10-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eventos', '0003_auto_20191020_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Evento', models.IntegerField()),
                ('email_Organizador', models.EmailField(max_length=254)),
                ('email_Usuario', models.EmailField(max_length=254)),
            ],
        ),
    ]
