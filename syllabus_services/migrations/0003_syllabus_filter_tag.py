# Generated by Django 5.0.1 on 2024-02-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_services', '0002_rename_syllsbus_syllabus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllabus',
            name='filter_tag',
            field=models.CharField(db_column='filter_tag', max_length=50, null=True),
        ),
    ]
