# Generated by Django 4.0.1 on 2022-01-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[('Software Developer', 1), ('QA', 2), ('DevOps', 3)], default=' 1 ', max_length=18),
            preserve_default=False,
        ),
    ]
