# Generated by Django 4.2.4 on 2024-07-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signin',
            name='phone',
            field=models.CharField(default='0779319357', max_length=10),
        ),
        migrations.AlterField(
            model_name='signin',
            name='gmail',
            field=models.EmailField(max_length=254),
        ),
    ]