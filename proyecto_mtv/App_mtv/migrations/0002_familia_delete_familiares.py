# Generated by Django 4.1.1 on 2022-09-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_mtv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fecha_nac', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Familiares',
        ),
    ]
