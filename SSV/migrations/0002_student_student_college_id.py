# Generated by Django 3.0.3 on 2020-03-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_college_id',
            field=models.IntegerField(default=False),
        ),
    ]
