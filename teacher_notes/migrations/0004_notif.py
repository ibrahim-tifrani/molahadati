# Generated by Django 4.2.4 on 2024-07-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_notes', '0003_rename_name_note1_name1_rename_note_note1_notes1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='notif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_teacher', models.CharField(blank=True, max_length=50)),
                ('conversation', models.TextField()),
            ],
        ),
    ]
