# Generated by Django 3.0.3 on 2020-03-29 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSV', '0005_auto_20200329_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_college_id',
            field=models.IntegerField(default=False, unique=True),
        ),
    ]
