# Generated by Django 2.1.5 on 2019-01-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.CharField(default='0000000', max_length=200),
        ),
    ]
