# Generated by Django 4.1.3 on 2022-12-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_project_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='progress_value',
            field=models.FloatField(default=0.0),
        ),
    ]
